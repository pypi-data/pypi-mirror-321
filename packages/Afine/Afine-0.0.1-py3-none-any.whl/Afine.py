from typing import List, Optional, Union, Tuple
import math
import torch
from torch import Tensor
from torch.optim.optimizer import (Optimizer, ParamsT, _use_grad_for_differentiable,_get_scalar_dtype)

__all__ = ['Afine',]

class Afine(Optimizer):
    def __init__(self,
                 params: ParamsT,
                 lr_rotate: Union[float, Tensor] = 1e-3,
                 lr_scale: Union[float, Tensor] = 1e-1,
                 lr_base: Union[float, Tensor] = 1e-6,
                 smooth: Union[float, Tensor] = 10,
                 weight_decay:  Union[float, Tensor] = 0,
                 eps: float = 1e-18,
                 ):
        
        if not lr_rotate>0:
            raise ValueError(f'Invalid 学习速率_向量旋转: {lr_rotate}')
        if not lr_scale>0:
            raise ValueError(f'Invalid 学习速率_向量缩放: {lr_scale}')
        if not lr_base>0:
            raise ValueError(f'Invalid 学习速率_基本: {lr_base}')

        if not smooth>=0: 
            raise ValueError(f'Invalid 平滑程度: {smooth}')

        if (not weight_decay>=0) or (not weight_decay<1):
            raise ValueError(f'Invalid 权重衰减: {weight_decay}')
        if not eps>0: 
            raise ValueError(f'Invalid eps:{eps}')

        
        defaults = dict(lr_rotate=lr_rotate,lr_scale=lr_scale,lr_base=lr_base,
                 smooth=smooth,weight_decay=weight_decay,
                 eps=eps,)
        super().__init__(params, defaults)

    

    def __setstate__(self, state):
        super().__setstate__(state)
        for group in self.param_groups:
            for p in group["params"]:
                p_state = self.state.get(p, [])
                if len(p_state) != 0 and not torch.is_tensor(p_state['warm']):
                    warm_val = float(p_state["warm"])
                    p_state["warm"] = torch.tensor(warm_val, dtype=_get_scalar_dtype())

    def _norm(self,x):
        return torch.linalg.norm(x.view(-1),ord=2,dim=0,keepdim=False)

    #@_use_grad_for_differentiable
    def step(self, closure=None, loss=None):
        self._cuda_graph_capture_health_check()

        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        if loss is None:
            loss=torch.tensor(1, dtype=_get_scalar_dtype())
            
        with torch.no_grad():
            for group in self.param_groups:
                for p in group['params']:
                    if not torch.isfinite(p.data).all():
                        print("tensor.data is not finite  --Optimizer")
                    p.data[~torch.isfinite(p.data)]=0
                    if p.requires_grad==False:
                        continue
                    if p.grad is None:
                        continue
                    if not torch.isfinite(p.grad).all():
                        print("tensor.grad is not finite  --Optimizer")
                    p.grad.data[~torch.isfinite(p.grad.data)]=0
                    if p.grad.data.is_sparse:
                        raise RuntimeError('AfineOptimizer does not support sparse gradients')
                    
                    state = self.state[p]  #get state dict for this param
                    if len(state) == 0:   #if first time to run...init dictionary with our desired entries
                        state['warm'] = torch.tensor(0, dtype=_get_scalar_dtype())
                        state['flatRotate'] = torch.zeros_like(p, memory_format=torch.preserve_format)
                        state['flatRotateNorm'] = torch.tensor(0, dtype=_get_scalar_dtype(),device=p.device)
                        state['flatScale'] = torch.tensor(1, dtype=_get_scalar_dtype(),device=p.device)
                        state['flatScaleNorm'] = torch.tensor(1, dtype=_get_scalar_dtype(),device=p.device)
                        state['flatBase'] = torch.zeros_like(p, memory_format=torch.preserve_format)
                        state['flatBaseAbs'] = torch.zeros_like(p, memory_format=torch.preserve_format)
                        
                    state['warm']=(state['warm']*group['smooth']+1)/(group['smooth']+1)

                    gradNorm=self._norm(p.grad)

                    source=p.data
                    sourceNorm=self._norm(source)
                    sourceNormalized=source/(sourceNorm+group['eps'])
                    target=sourceNormalized-(p.grad*(group['lr_rotate']/(gradNorm+group['eps'])))
                    targetNormalized=target/(self._norm(target)+group['eps'])
                    
                    rotate=targetNormalized-sourceNormalized
                    rotate[~torch.isfinite(rotate)]=0
                    
                    rotateNorm=self._norm(rotate)
                    rotateNorm[~torch.isfinite(rotateNorm)]=0
                    
                    state['flatRotate']=(state['flatRotate']*group['smooth']+rotate*state['warm'])/(group['smooth']+state['warm'])
                    state['flatRotateNorm']=(state['flatRotateNorm']*group['smooth']+rotateNorm)/(group['smooth']+1)
                    rotate*=(sourceNorm*self._norm(state['flatRotate'])/(state['flatRotateNorm']+group['eps']))
                    
                    rotate[~torch.isfinite(rotate)]=0
                    state['flatRotate'][~torch.isfinite(state['flatRotate'])]=0
                    state['flatRotateNorm'][~torch.isfinite(state['flatRotateNorm'])]=0
                    
                    #target=source+rotate #最后统一应用
                    

                    target=sourceNormalized-(p.grad*(group['lr_scale']/(gradNorm+group['eps'])))
                    #targetNorm=self._norm(target)
                    targetNorm=(target.view(-1)*sourceNormalized.view(-1)).sum(dim=0,keepdim=False)
                    targetNorm.clamp(min=0)
                    
                    scale=(targetNorm+group['eps'])
                    scale[(~torch.isfinite(scale))|(scale<=0)]=1
                    
                    state['flatScale']=((state['flatScale']**group['smooth'])*(scale**state['warm']))**(1/(group['smooth']+state['warm']))
                    state['flatScale'][(~torch.isfinite(state['flatScale']))|(state['flatScale']<=0)]=1
                    
                    scaleNorm=torch.maximum(scale,1/scale)
                    
                    state['flatScaleNorm']=((state['flatScaleNorm']**group['smooth'])*(scaleNorm))**(1/(group['smooth']+1))
                    state['flatScaleNorm'][(~torch.isfinite(state['flatScaleNorm']))|(state['flatScaleNorm']<=0)]=1
                    
                    if group['weight_decay']>0:
                        #scale=torch.minimum(((scale-1)*group['weight_decay']).asinh()/group['weight_decay']+1,scale)
                        scale=((scale)*group['weight_decay']).asinh()/group['weight_decay']
                    scale**=(self._norm(state['flatScale'])/state['flatScaleNorm'])
                    scale[~torch.isfinite(scale)]=1
                    scale[scale<0]=0
                    
                    #target=source*scale #最后统一应用
                    
                    k=p.grad.abs()/(state['flatBaseAbs']+group['eps']+(1-state['warm']))
                    state['flatBaseAbs']=(state['flatBaseAbs']*group['smooth']+p.grad.abs()*k)/(group['smooth']+k)
                    k=k*state['warm']
                    state['flatBase']=(state['flatBase']*group['smooth']-p.grad*k)/(group['smooth']+k)
                    #base=-p.grad*((group['lr_base']*self._norm(state['flatBase']))/(state['flatBaseNorm']*gradNorm+group['eps']))
                    base=group['lr_base']*state['flatBase']/state['flatBaseAbs']
                    
                    base[~torch.isfinite(base)]=0
                    state['flatBase'][~torch.isfinite(state['flatBase'])]=0
                    state['flatBaseAbs'][~torch.isfinite(state['flatBaseAbs'])]=0
                    
                    #target=source+base #最后统一应用
                    

                    dataNorm0=self._norm(p.data)
                    p.data+=rotate
                    p.data*=(scale*dataNorm0)/(self._norm(p.data)+group['eps'])
                    p.data+=base
                    p.data[~torch.isfinite(p.data)]=0
                    
        return loss
