# Afine Optimizer
An optimizer that is superior to Adam. Based on @PyTorch

The training is more stable and reaches a more **elegant** optimal solution faster.

![image](rendering.png)
![image](renderingZoom.png)

## 思路说明
把每组参数看作高维向量. 优化步骤被分割为3个过程: 旋转、缩放、平移. 使用三个学习率分别控制三个过程的调整量. 

1.旋转
- 计算梯度对参数向量方向的影响.
- 根据旋转的稳定程度调整旋转的作用强度. 
- 使用近似旋转改变参数向量方向而不改变模长.

2.缩放
- 计算梯度对参数向量模长的影响.
- 根据模长改变的稳定程度调整缩放的作用强度.
- 权重衰减作用于这一步: 使用ArcSinh函数对向量放大带来阻力而促进向量缩小.
- 应用缩放变换.

3.平移
- 旋转和缩放对零向量无作用, 为使零初始化和模长较小的向量也能被训练, 需加入平移.
- 此处的平移带有惯性,且平移量与梯度稳定程度有关.

## Demo程序
demo程序在test.py文件中,直接运行即可得到此页面中Affine与RAdam的对比图.(依赖visdom)
demo中构建了一个神经网络用简陋的方式对一个包含动态随机参数的公式生成的周期性曲线进行预测.

## Install
```bash
pip install afine
```

## Use
```python
from Afine import Afine
...
optimizer=Affine(moduel.parameters(),lr_rotate = lr_rotate,lr_scale = lr_scale,lr_base = lr_base,weight_decay=weight_decay)
```

## HomePage
<https://github.com/PsycheHalo/Afine/>
