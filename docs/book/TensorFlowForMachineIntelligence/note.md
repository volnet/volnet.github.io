面向机器智能的TensorFlow实践
==============================

![](contents/cover.jpg)

作者：Sam Abrahams, Danijar Hafner, Erik Erwitt, Ariel Scarpinelli 著

段菲 陈澎 译

译者序
------------------------------

TensorFlow是Google的第二代分布式机器学习框架。

TensorFlow的“不足”较为突出，接口过于复杂，对初学者的编程技能和知识水平要求偏高，学习曲线过陡。

这不是一本机器学习理论或深度学习的入门读物，阅读本书需要对经典机器学习理论和算法、深度卷积网络、循环神经网络的基本原理有初步了解，并对Python编程和常用的Python库（如NumPy和matplotlib）较为熟悉。

这本书的代码是基于0.8版的，译者对0.9版所做的接口变动以“译者注”的形式做了部分说明。

前言
------------------------------

通过这一节，讲述了本书的主体结构。同时指出了“其他机器学习库”：

- Caffe 专注于卷积神经网络和图像处理，使用C++语言编写。
- Chainer 是另一个灵活的机器学习Python库，支持单机多GPU运算。
- CNTK 是微软公司的首个开源机器学习库，它拥有自己的模型定义语言，支持声明式的分布式模型构建。
- Deeplearning4j 是一个专门针对神经网络的Java库，它易于与Spark、Hadoop和其他基于Java的分布式软件集成，具有良好的可伸缩性。
- Nervana Neon 是一个高效的Python机器学习库，支持单机多GPU运算。
- Theano 是一个极为灵活的Python机器学习库，因其出众的用户友好性以及可以用异常简单的方式定义复杂模型等特点，在科研领域深受欢迎。TensorFlow的API与Theano API最为相似。
- Torch 是一个专注于GPU实现的机器学习库，它是用Lua语言编写的，并由来自若干家大公司的研究团队提供支持。 

第一部分 开启TensorFlow之旅
------------------------------

第1章 引言
------------------------------

### 1.1 无处不在的数据

各种数据从无穷无尽的渠道不断涌入，存储以PB为单位存储。

计算机性能也持续提升。虽然CPU的发展速度放缓，但是并行处理架构取得了爆炸式的发展。GPU也被大量运用于通用计算领域。

近年来，一种特殊类型的机器学习范式在几乎所有领域都取得了无数巨大的成功，它就是深度学习。

### 1.2 深度学习

深度学习是指多层神经网络。它是一类极为灵活的可利用种类繁多的数学方法以及不同数学方法组合的模型。这类模型极为强大，但直到最近几年，人们才有能力卓有成效地利用神经网络，其背后原因：

- 获取足够量的数据成为现实（数据越来也多）
- GPU快速发展，多层神经网络拥有了超越其他机器学习方法所必须的计算能力。
- 更有效的训练算法（by译者）

一个调校好的深度学习模型可以接收所有的参数，并自动确定输入值的有用高阶组合。

相关数学概念几十年前便提出，但致力于创建和训练这些深度模型的编程库是近年才出现的。

深度学习长期面临的两个问题：

- 灵活性：这些编程库在灵活性和生产价值之间进行取舍
- 研究和生产使用不同类型的库：即便出现了可托管在分布式硬件上的快速、高效的库，但它们往往专注于特定类型的神经网络，并不适合研究新的和更好的模型。

TensorFlow就是为了在上面二者之间取得平衡而设计的。

### 1.3 TensorFlow：一个现代的机器学习库

TensorFlow的前身：[DistBelief](https://static.googleusercontent.com/media/research.google.com/zh-CN//archive/large_deep_networks_nips2012.pdf)

它的设计目标：

- 灵活性
- 高效性
- 良好的可扩展性
- 可移植性：任何形式和尺寸的计算机都可以运行。

如果你和你的同事：

- 拥有数据
- 一个有待求解的问题
- 一台可工作的计算机

TensorFlow正是你们一直寻找的“武林秘籍”。

### 1.4 TensorFlow：技术概要

TensorFlow的前身[DistBelief](https://static.googleusercontent.com/media/research.google.com/zh-CN//archive/large_deep_networks_nips2012.pdf)来自于Google Brain团队。TensorFlow汲取了它的经验和教训，现已被成功运用于自然语言处理、人工智能、计算机视觉和预测分析等领域。

### 1.5 何为TensorFlow

在TensorFlow的官网有两句话：

> TensorFlow is an Open Source Software Library for Machine Intelligence

> TensorFlow is an open source software library for numerical computation using data flow graphs.

后面一个声明体现了TensorFlow的几个特点：

- open source（开源）
- library for numerical computation（数值计算库）：TensorFlow提供了一个可使用户用数学方法从零开始定义模型的函数和类的广泛套件。这使得具有一定技术背景的用户可迅速而直观地创建自定义的、具有较高灵活性的模型。
- data flow graphs（数据流图）：可以直观地体现将一个计算任务拆分成多个计算任务的过程。
- 分布式功能
- 软件套件
    - TensorFlow：用于定义模型，由C++写成，有Python接口
    - TensorBoard：可视化软件
    - TensorFlow Serving：可以运行模型的服务器，只有C++接口

### 1.6 何时使用TensorFlow

- 研究、开发和迭代新的机器学习架构。
- 将模型从训练直接切换到部署。
- 实现已有的复杂架构。
- 大规模分布式模型。
- 为移动／嵌入式系统创建和训练模型。

### 1.7 TensorFlow的优势

- 易用性：稳定的API、与NumPy兼容、不用编译、有多种高层接口如Keras和SkFlow
- 灵活性：各种设备都可以使用、分布式可提高速度、可以同时利用CPU和GPU
- 高效性：性能好、且有开放的社区使它更好
- 幕后支持：谷歌支持、社区支持好、已经发布了多个免费模型
- 额外特性：TensorBoard提供的可视化和TensorFlowServing提供的能力是其他平台所没有的

### 1.8 使用TensorFlow所面临的挑战

- 分布式支持尚不成熟
- 实现定制代码的技巧性较强
- 某些特性仍然缺失

### 1.9 高歌猛进

后续将对它的安装、核心库和环境进行全面讲解。

第2章 安装TensorFlow
------------------------------

### 2.1 选择安装环境

为了避免软件包依赖，作者介绍了三种方法：

- 代码库内部的软件包依赖：重复太多，不推荐
- 使用依赖环境：Python的标准版则使用Virtualenv或者[Anaconda](https://www.continuum.io/anaconda-overview)的话，则使用[Conda](https://conda.io/docs/)
- 使用容器：步骤略多一点，适用于部署到一台或多台服务器。

### 2.2 Jupyter Notebook与matplotlib

Jupyter Notebook可交互式地编写包含代码、文本、输出、LaTeX及其他可视化结果的文档。

典型的TensorFlow程序已经被划分为“计算图的定义”和“运行计算图”两部分。

matplotlib是一个绘图库，它允许用户使用Python创建动态的、自定义的可视化结果。

### 2.3-2.7 [省略]

这几节主要讲述的是安装的过程，与[官方文档](https://www.tensorflow.org/versions/master/install/install_linux)描述基本一致，但我各种原因没有成功。还好有Docker安装的方案，参考[官方文档](https://hub.docker.com/r/tensorflow/tensorflow/)

```
docker run -it -p 8888:8888 tensorflow/tensorflow
```

### 2.8 测试TensorFlow、Jupyter Notebook及matplotlib

在Jupyter Notebook中，New一个Python2的Notebook，输入下面的代码

```
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
```

```
%matplotlib inline 
a = tf.random_normal([2,20])
sess = tf.Session()
out = sess.run(a)
x, y = out

plt.scatter(x, y)
plt.show()
```

%matplotlib inline这是一条专门的命令，用于通知笔记本将matplotlib图表直接显示在浏览器中。

下面逐行分析代码：

1. 用TensorFlow定义一个由随机数构成的2X20的矩阵，并将其赋给变量a。
2. 启动TensorFlow Session，并将其赋予一个sess对象。
3. 用sess.run()方法执行对象a，并将输出（NumPy数组）赋给out。
4. 将这个2X20的矩阵划分为两个1X10的向量x和y。
5. 利用pyplot模块绘制散点图，x对应横轴，y对应纵轴。

![](contents/chapter02/001.png)

第二部分 TensorFlow与机器学习基础
------------------------------

第3章 TensorFlow基础 
------------------------------

### 3.1 数据流图简介

#### 3.1.1 数据流图基础

作者从一个最简单的数据流图开始，仅包含两个输入，一个圆形，以及一个输出。其中圆形代表节点，而输入和输出的箭头代表边。

- 节点（node）：通常以圆圈、椭圆、方框来表示，代表了对数据所做的运算或某种操作。
- 边（edge）：对应于Operation传入和Operation传出，通常以箭头表示。

接下来，是一个更符合实际使用的流图，有input的概念。

- input节点，只负责输入，而不需要在数据输入的环节，显示调用内部的运算节点，只需要将数据准备好即可。
- 执行顺序：不同节点之间的计算顺序是无法估计的。

#### 3.1.2 节点的依赖关系

- 直接依赖：a->b，则b直接依赖于a
- 间接依赖：a->b->c，则c间接依赖于a
- 循环依赖：TensorFlow无法执行循环依赖，因为它有很多问题，比如计算无限循环，依赖节点数量变得无穷大，数值上溢、下溢或者趋近于0从而变得没有意义。

可以使用数据流图的“展开”（unrolling）来处理循环依赖的问题，将一个循环依赖的问题，横向摆开有限次。

### 3.2 在TensorFlow中定义数据流图

TensorFlow的工作流非常容易记忆，它只包含两个步骤：

1. 定义数据流图。
2. 运行数据流图（在数据上）。

#### 3.2.1 构建第一个TensorFlow数据流图

```
import tensorflow as tf

a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.multiply(a, b, name="mul_c")
d = tf.add(a, b, name="add_d")
e = tf.add(c, d, name="add_e")

sess = tf.Session()
output = sess.run(e)

```

TensorFlow Session对象在运行时负责对数据流图进行监督，并且是运行数据流图的主要接口。

在上面的例子之后，我们可以将这个数据流图保存下来，原著中的版本不再适用于APIr1.2，这里我做了更新。（[参考这里>>](https://github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/tensorboard/README.md)）

```
writer = tf.summary.FileWriter('./my_graph', sess.graph)
```

这样在根目录就多出一个`my_graph`文件夹。

可以使用`tensorboard --logdir="my_graph"`，打开tensorboard，并点击Graph菜单，可以看到我们刚刚用python代码编写的数据流图的图形化表示。

完成数据流图的构造之后，需要将对象关闭，可以使用下面的语句。

```
writer.close()
sess.close()
```

> 补充说明：因为这里我们使用了docker的方式来运行，和之前介绍的启动docker的默认方法不同，我们使用了下面的语句：

```
docker run -it -p 6006:6006 -p 8888:8888 tensorflow/tensorflow /bin/bash
```

> 这样就进入了命令行模式。如果出现了docker无法exit的情况（There are stopped jobs.），可以使用`jobs -l`查看未停止的jobs，然后用`kill %1`来杀死这个进程，其中这个1是job的编号。

#### 3.2.2 张量思维

#### 3.2.3 张量的形状

#### 3.2.4 TensorFlow的Operation

#### 3.2.5 TensorFlow的Graph对象

#### 3.2.6 TensorFlow Session

#### 3.2.7 利用占位符点添加输入

#### 3.2.8 Variable对象

### 3.3 通过名称作用域组织数据流图

### 3.4 练习：综合运用各种组件

#### 3.4.1 构建数据流图

#### 3.4.2 运行数据流图

### 3.5 本章小结

第4章 机器学习基础
------------------------------

第三部分 用TensorFlow实现更高级的深度模型
------------------------------

第5章 目标识别与分类
------------------------------

第6章 循环神经网络与自然语言处理
------------------------------

第四部分 其他提示、技术与特性
------------------------------

第7章 产品环境中模型的部署
------------------------------

第8章 辅助函数、代码结构和类
------------------------------