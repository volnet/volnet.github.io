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

![](contents/chapter03/001.png)

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

> 这样就进入了命令行模式。在命令行下，使用python shell执行上面所列出来的python脚本，然后再在宿主服务器上通过`http://localhost:6006`访问tensorboard。
> 如果出现了docker无法exit的情况（There are stopped jobs.），可以使用`jobs -l`查看未停止的jobs，然后用`kill %1`来杀死这个进程，其中这个1是job的编号。

> 上面的方法虽然搞定了tensorboard，但是无法同时使用jupyter notebook和tensorboard，而且每次关闭后，之前保存的东西就没有了，为此我做了个持久化的版本，详见这里：[volnet/tf-notebook](https://hub.docker.com/r/volnet/tf-notebook/)或者[volnet/tf-tensorboard](https://hub.docker.com/r/volnet/tf-tensorboard/)。

#### 3.2.2 张量思维

所谓张量，即n维矩阵的抽象。因此，1D张量等价于向量，2D张量等价于矩阵，对于更高维数的张量，可称“N维张量”或“N阶张量”。

![](contents/chapter03/002.png)

```
import tensorflow as tf

a = tf.constant([5,3], name="input_a")
b = tf.reduce_prod(a, name="prod_b")
c = tf.reduce_sum(a, name="sum_c")
d = tf.add(c, d, name="add_d")
```

1. Python原生类型：TensorFlow可以接收Python数值、布尔值、字符串或由它们构成的列表。但是TensorFlow的类型比Python的类型分地更细，如数值型，TensorFlow有很多种，而Python只有一种。
2. NumPy数组：TensorFlow的数据类型是基于NumPy的数据类型的。实际上，语句np.int32==tf.int32的结果为True。但是字符串数据类型，受限于NumPy中并无与tf.string精确对应的类型，因此TensorFlow可以从NumPy中完美地导入字符串数组，只是不要在NumPy中显式指定dtype属性。

```
import numpy as np

# 元素类型为32位整数的0阶张量
t_0 = np.array(50, dtype=np.int32)

# 元素为字节字符串类型的1阶张量
# 注意：在NumPy中使用字符串时，不要显式指定dtype属性
t_1 = np.array([b"apple", b"peach", b"grape"])

# 元素为布尔型的2阶张量
t_2 = np.array([[True, False, False],
                [True, False, False],
                [True, False, False]],
                dtype=np.bool)

# 元素为64位整数的3阶张量
t_3 = np.array([[ [0,0], [0,1], [0,2] ],
                [ [0,0], [0,1], [0,2] ],
                [ [0,0], [0,1], [0,2] ]]
                dtype=np.int64)
```

#### 3.2.3 张量的形状

shape是TensorFlow的专有术语，它同时刻画了张量的维（阶）数以及每一维的长度。

既可以列表（list）也可以用列表（tuple）来描述张量的形状（shape）。

除了能够将张量的每一维指定为固定长度

```
# 具有任意长度的向量的形状
s_1_flex = [None]

# 行数任意、列数为3的矩阵的形状
s_2_flex = (None, 3)

# 第1维上长度为2，第2维和第3维上长度任意的3阶张量
s_3_flex = [2, None, None]

# 形状可为任意值的张量
s_any = None
```

如果需要在数据流图的中间获取某个张量的形状，可以使用tf.shape Op。它的输入为希望获取其形状的Tensor对象，输出为一个int32的向量：

```
import tensorflow as tf

# ...创建某种类型的神秘张量

# 获取上述张量的形状
shape = tf.shape(mystery_tensor, name="mystery_shape")
```

#### 3.2.4 TensorFlow的Operation

Op是一些对（或利用）Tensor对象执行运算的节点。计算完毕后，它们会返回0个或多个张量，可在以后为数据流图中的其他Op所使用。

- 无输入、输出的运算：有些Op没有输入也没有输出，Op并不只限于计算，也可以用于如状态初始化这样的任务（非数学Op）。

##### 运算符重载

也可以用`c=a+b`来表示`c = tf.add(a, b)`。

![](contents/chapter03/003.png)

#### 3.2.5 TensorFlow的Graph对象

创建一个新的数据流图可以通过`tf.Graph()`来完成，默认的情况下，并不需要用户自行创建一个Graph对象，TensorFlow库在被加载时，它会自动创建一个Graph对象，并将其作为默认的数据流图。

```
import tensorflow as tf

# 创建一个新的数据流图
g = tf.Graph()
```

下面的方法可以拿到默认的Graph对象。

```
import tensorflow as tf

# 获得默认数据流图的句柄
default_graph = tf.get_default_graph()
```

我们还可以使用`with`语句，切换当前的默认Graph对象。

```
import tensorflow as tf

g = tf.Graph()
with g.as_default():
    # 像往常一样创建一些Op；它们将被添加到Graph对象g中
    a = tf.multiply(2, 3)

# 由于不在with语句块中，下面的Op将放置在默认数据流图中
also_in_default_graph = tf.subtract(5,1)
```

当需要在单个文件中定义多个数据流图时，最佳实践是**不适用默认数据流图，或为其立即分配句柄**。这样可以保证各节点按照一致的方式添加到每个数据流图中。

#### 3.2.6 TensorFlow Session

Session类负责数据流图的执行。构造方法tf.Session()接收3个可选参数：

- target指定了所要使用的执行引擎。对于大多数应用，该参数取为默认的空字符串。在分布式设置中使用Session对象时，该参数用语连接不同的tf.train.Server实例
- graph参数指定了将要在Session对象中加载的Graph对象，其默认值为None，表示将使用当前默认数据流图。
- config参数允许用户指定配置Session对象所需的选项，如限制CPU或GPU的使用数目，为数据流图设置优化参数及日志选项等。

一旦创建完Session对象，便可利用其主要的方法run()来计算所期望的Tensor对象的输出：

[Session.run()](https://www.tensorflow.org/api_docs/python/tf/Session#run)方法接收一个参数fetches，以及其他三个可选参数（`feed_dict`，`options`，`run_metadata`）：

- fetches参数：可以传入张量也可以传入Op，可以是单个数值也可以是个数组
- feed_dict参数：用于覆盖数据流图中的Tensor对象值，它需要Python字典对象作为输入。它可以替代TensorFlow中的中间值，在一个规模较大的数据流图中，可以利用它提供一些虚构的值对某些部分进行测试。
- options、run_metadata尚在实验阶段。

Session使用完了之后需要调用`.close()`关闭。

#### 3.2.7 利用占位符点添加输入

占位符的行为与Tensor对象一致，但在创建时无须为它们指定具体的数值。它们的作用是为运行时即将到来的某个Tensor对象预留位置，因此实际上变成了“输入”节点。

```
import tensorflow as tf
import numpy as np

# 创建一个长度为2、数据类型为int32的占位向量
a = tf.placeholder(tf.int32, shape=[2], name="my_input")

# 将该占位向量视为其他任意Tensor对象，加以使用
b = tf.reduce_prod(a, name="prod_b")
c = tf.reduce_sum(a, name="prod_c")

d = tf.add(b, c, name="add_d")

# 定义一个TensorFlow Session对象
sess = tf.Session()

# 创建一个将传给feed_dict参数的字典
# 键：'a'，指向占位符输出Tensor对象的句柄
# 值：一个值为[5,3]、类型为int32的向量
input_dict = {a: np.array([5,3], dtype=np.int32)}

# 计算d的值，将input_dict的“值”传给a
sess.run(d, feed_dict=input_dict)
```

placeholder的值是无法计算的——如果试图将其传入Session.run()，将引发一个异常。

#### 3.2.8 Variable对象

创建Variable对象

Tensor对象和Op对象都是不可变的（immutable），但机器学习任务的本质决定了需要一种机制保存随时间变化的值。

可以通过`tf.Variable()`创建对象。

```
import tensorflow as tf

# 为Variable对象传入一个初始值3
my_var = tf.Variable(3, name="my_variable")

add = tf.add(5, my_var)
mul = tf.multiply(8, my_var)

sess = tf.Session()
print( sess.run(add, {my_var: 3}) )
print( sess.run(mul, {my_var: 3}) )
```

TensorFlow提供了大量的辅助Op用于初始化`tf.zeros()`、`tf.ones()`、`tf.random_normal()`、`tf.random_uniform()`，每个Op都接收一个shape参数，以指定所创建的Tensor对象的形状。

```
import tensorflow as tf

# 2x2的零矩阵
zeros = tf.zeros([2, 2])

# 长度为6的全1向量
ones = tf.ones([6])

# 3x3x3的张量，其元素服从0~10的均匀分布
uniform = tf.random_uniform([3, 3, 3], minval=0, maxval=10)

# 3x3x3的张量，其元素服从0均值、标准差为2的正态分布
normal = tf.random_normal([3, 3, 3], mean=0.0, stddev=2.0)

# 3x3x3的张量，其元素服从任何偏离均值不会超过2倍标准差的值，从而可以防止有一个或两个元素与该张量中的其他元素显著不同的情况出现
truncated = tf.truncated_normal([3, 3, 3], mean=5.0, stddev=1.0)

sess = tf.Session()
out_zeros = sess.run(zeros)
out_ones = sess.run(ones)
out_uniform = sess.run(uniform)
out_normal = sess.run(normal)
out_truncated = sess.run(truncated)

print( out_zeros )
print( out_ones )
print( out_uniform )
print( out_normal )
print( out_truncated )
```

Variable对象的初始化

可以使用`tf.global_variables_initializer()`（原书使用`tf.initialize_all_variables()`）Op传给Session.run()完成的。

> WARNING:tensorflow:From /usr/local/lib/python2.7/dist-packages/tensorflow/python/util/tf_should_use.py:170: initialize_all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2017-03-02.
> Instructions for updating:
> Use `tf.global_variables_initializer` instead.

如果只需要对数据流图中定义的一个Variable对象子集初始化，可使用`tf.initialize_variables()`。

```
import tensorflow as tf

var1 = tf.Variable(0, name="initialize_me")
var2 = tf.Variable(1, name="no_initialization")

#init = tf.initialize_variables([var1], "init_var1")
init = tf.variables_initializer([var1], "init_var1")

sess = tf.Session()
out = sess.run(init)

print(out)
```

Variable对象的修改

要修改Variable对象的值，可使用`Variable.assign()`方法。该方法的作用是为Variable对象赋予新值。需要注意的是，Variable.assign()是一个Op，要使其生效必须在一个Session对象中运行：

```
import tensorflow as tf

# 创建一个初值为1的Variable对象
my_var = tf.Variable(1)

# 创建一个Op，使其在每次运行时都将该Variable对象乘以2
my_var_times_two = my_var.assign(my_var * 2)

# 初始化Op
init = tf.global_variables_initializer()

sess = tf.Session()

# 初始化Variable对象
sess.run(init)

# 将Variable对象乘以2，并将其返回
out1 = sess.run(my_var_times_two)
print(out1)
# 输出：2

# 将Variable对象乘以2，并将其返回
out2 = sess.run(my_var_times_two)
print(out2)
# 输出：4

# 将Variable对象乘以2，并将其返回
out3 = sess.run(my_var_times_two)
print(out3)
# 输出：8
```

对于Variable对象的简单自增和自减，TensorFlow提供了`Variable.assign_add()`方法和`Variable.assign_sub()`

```
import tensorflow as tf

my_var = tf.Variable(1)
out1 = my_var.assign_add(5)
out2 = my_var.assign_sub(2)

# 初始化Op
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
print( sess.run(out1) )
## 6
print( sess.run(out2) )
## 4

# 如果希望将所有Variable对象的值重置为初始值，则只需要再次调用global_variables_initializer，也就是运行sess.run(init)
sess.run(init)
print( sess.run(out2) )
## -1
```

### 3.3 通过名称作用域组织数据流图

名称作用域的基本用法是将Op添加到`with tf.name_scope(<name>):`语句块中，且名称作用域可以嵌套。

```
import tensorflow as tf

graph = tf.Graph()

with graph.as_default():
    in_1 = tf.placeholder(tf.float32, shape=[], name="input_a")
    in_2 = tf.placeholder(tf.float32, shape=[], name="input_b")
    const = tf.constant(3, dtype=tf.float32, name="static_value")
    
    with tf.name_scope("Transformation"):
        
        with tf.name_scope("A"):
            A_mul = tf.multiply(in_1, const)
            A_out = tf.subtract(A_mul, in_1)
            
        with tf.name_scope("B"):
            B_mul = tf.multiply(in_2, const)
            B_out = tf.subtract(B_mul, in_2)
            
        with tf.name_scope("C"):
            C_div = tf.div(A_out, B_out)
            C_out = tf.add(C_div, const)
            
        with tf.name_scope("C"):
            D_div = tf.div(B_out, A_out)
            D_out = tf.add(D_div, const)
            
writer = tf.summary.FileWriter('../logs', graph=graph)
print("ok")
writer.close()
```

使用TensorBoard显示如下：

![](contents/chapter03/004.png)

### 3.4 练习：综合运用各种组件

#### 3.4.1 构建数据流图

```
import tensorflow as tf
graph = tf.Graph()
with graph.as_default():
    with tf.name_scope("variables"):
        # 记录数据流图运行次数的Variable对象
        global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name="global_step")
        
        # 追踪该模型的所有输出随时间的累加和的Variable对象
        total_output = tf.Variable(0.0, dtype=tf.float32, trainable=False, name="total_output")
    with tf.name_scope("transformation"):
        with tf.name_scope("input"):
            # 创建输出占位符，用于接收一个向量
            a = tf.placeholder(tf.float32, shape=[None], name="input_placeholder_a")
        
        with tf.name_scope("intermediate_layer"):
            b = tf.reduce_prod(a, name="product_b")
            c = tf.reduce_sum(a, name="sum_c")
            
        # 独立的输出层
        with tf.name_scope("output"):
            output = tf.add(b, c, name="output")
    with tf.name_scope("update"):
        # 用最新的输出更新Variable对象total_output
        update_total = total_output.assign_add(output)
        # 将前面的Variable对象global_step增1，只要数据流图运行，该操作便需要运行
        increment_step = global_step.assign_add(1)
    with tf.name_scope("summaries"):
        avg = tf.div(update_total, tf.cast(increment_step, tf.float32), name="average")
        
        # 为输出节点创建汇总数据
        tf.summary.scalar(b'Output', output)
        tf.summary.scalar(b'Sum_of_outputs_over_time', update_total)
        tf.summary.scalar(b'Average_of_outputs_over_time', avg)
    with tf.name_scope("global_ops"):
        # 初始化Op
        init = tf.global_variables_initializer()
        # 将所有汇总数据合并到一个Op中
        merged_summaries = tf.summary.merge_all()
# 用明确创建的Graph对象启动一个会话
sess = tf.Session(graph=graph)
# 开启一个Summary.FileWriter对象，保存汇总数据
writer = tf.summary.FileWriter('../logs', graph=graph)
# 初始化Variable对象
sess.run(init)

def run_graph(input_tensor):
    """
    辅助函数；用给定的输入张量运行数据流图，并保存汇总数据
    """
    feed_dict = {a: input_tensor}
    _, step, summary = sess.run([output, increment_step, merged_summaries], feed_dict=feed_dict)
    writer.add_summary(summary, global_step=step)
    
    
# 用不同的输入运行该数据流图
run_graph([2, 8])
run_graph([3, 1, 3, 3])
run_graph([8])
run_graph([1, 2, 3])
run_graph([11, 4])
run_graph([4, 1])
run_graph([7, 3, 1])
run_graph([6, 3])
run_graph([0, 2])
run_graph([4, 5, 6])

# 将汇总数据写入磁盘
writer.flush()

# 关闭Summary.FileWriter对象
writer.close()

# 关闭Session对象
sess.close()
```

#### 3.4.2 运行数据流图

展开GRAPHS菜单可以看到以上代码的图形化展示：

![](contents/chapter03/005.png)

展开SCALARS菜单可以看到最后的输出结果：

![](contents/chapter03/005.png)

### 3.5 本章小结

本章介绍了TensorFlow的基础内容，后续将学习机器学习。

第4章 机器学习基础
------------------------------

### 4.1 有监督学习简介

在这类问题中，我们的目标是依据某个带标注信息的输入数据集（即其中的每个样本都标注了真实的或期望的输出）去训练一个推断模型。该模型应能覆盖一个数据集，并可对不存在于初始训练集中的新样本的输出进行预测。

推断模型即运用到数据上的一系列数学运算。具体的运算步骤是通过代码设置的，并由用语求解某个给定问题的模型确定。模型确定后，构成模型的运算也就固定了。在各运算内部，有一些与其定义相关的数值，如“乘以3”、“加2”。这些值都是模型的参数，且在训练过程中需要不断更新，以使模型能够学习，并对其输出进行调整。

虽然不同的推断模型在所使用的运算的数量、运算的组合方式以及所使用的参数数量上千差万别，但对于训练，我们始终可采用相同的一般结构：

![](contents/chapter04/001.png)

书中创建了一个训练闭环，它具有如下功能：

1. 对模型参数初始化。通常采用对参数随机赋值的方法，但对于比较简单的模型，也可以将各参数的初值均设为0。
2. 读取训练数据（包括每个数据样本及期望输出）（inputs）。通常人们会在这些数据送入模型之前，随机打乱样本的次序。
3. 在训练数据上执行推断模型（inference）。这样，在当前模型参数配置下，每个训练样本都会得到一个输出值。
4. 计算损失（loss）。损失是一个能够刻画模型在最后一步得到的输出与来自训练集的期望输出之间差距的概括性指标。
5. 调整模型参数（train）。这一步对应于实际的学习过程。给定损失函数，学习的目的在于通过大量训练步骤改善各参数的值，从而将损失最小化。最常见的策略是使用梯度下降算法。

上述闭环会依据所需的学习速率、所给定的模型及其输入数据，通过大量循环不断重复上述过程。

当训练结束后，便进入评估阶段（evaluate）。在这一阶段中，我们需要对一个同样含有期望输出信息的不同测试集依据模型进行推断，并评估模型在该数据集上的损失。该测试集中包含了何种样本，模型是预先无法获悉的。通过评估，可以了解到所训练的模型在训练集之外的推广能力。一种常见的方法是将原始数据集一分为二，将70%的样本用于训练，其余30%的样本用于评估。

```
import tensorflow as tf

# 初始化变量和模型参数，定义训练闭环中的运算

def inference(X):
    # 计算推断模型在数据X上的输出，并将结果返回
def loss(X, Y):
    # 依据训练数据X及其期望输出Y计算损失
def inputs():
    # 读取或生成训练数据X及其期望输出Y
def train(total_loss):
    # 依据计算的总损失训练或调整模型参数
def evaluate(sess, X, Y):
    # 对训练得到的模型进行评估
    
# 在一个会话对象中启动数据流图，搭建流程
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    
    X, Y = inputs()
    total_loss = loss(X, Y)
    train_op = train(total_loss)
    
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    
    # 实际的训练迭代次数
    training_steps = 1000
    for steps in range(training_steps):
        sess.run([train_op])
        # 出于调试和学习的目的，查看损失在训练过程中递减的情况
        if step % 10 == 0:
            print "loss: ", sess.run([total_loss])
            
    evaluate(sess, X, Y)
    
    coord.request_stop()
    coord.join(threads)
    sess.close()
```

### 4.2 保存训练检查点

为了避免多个训练周期运行的过程失败（如断电等原因），内存中的数据丢失，TensorFlow提供了保存检查点的方法。

`tf.train.Saver`可以用来存储。

```
saver.save(sess, 'my-model', global_step=0) ==> filename: 'my-model-0'
...
saver.save(sess, 'my-model', global_step=1000) ==> filename: 'my-model-1000'
```

`tf.train.get_checkpoint_state`可以用于验证之前是否有检查点文件被保存下来，可以使用`tf.train.Saver.restore`来恢复。

### 4.3 线性回归

线性回归的目标是找到一个与这些数据最为吻合的线性函数。

```
import tensorflow as tf

# w1, w2, ..., wk为模型从训练数据中学习到的参数，或赋予每个变量的“权值”
W = tf.Variable(tf.zeros([2,1]), name="weights")
# b也是一个学习到的参数，这个线性代数中的常量也称为模型的偏置（bias）
b = tf.Variable(0., name="bias")

# 初始化变量和模型参数，定义训练闭环中的运算

def inference(X):
    # 计算推断模型在数据X上的输出，并将结果返回
    return tf.matmul(X, W) + b
def loss(X, Y):
    # 依据训练数据X及其期望输出Y计算损失
    Y_predicted = inference(X)
    return tf.reduce_sum(tf.squared_difference(Y, Y_predicted))
def inputs():
    # 读取或生成训练数据X及其期望输出Y
    weight_age = [[84,46],[73,20],[65,52],[70,30],
                 [76,57],[69,25],[63,28],[72,36],[79,57],[75,44],
                 [27,24],[89,31],[65,52],[57,23],[59,60],[69,48],
                 [60,34],[79,51],[75,50],[82,34],[59,46],[67,23],
                 [85,37],[55,40],[63,30]]
    blood_fat_content = [354,190,405,263,451,302,288,
                        385,402,365,209,290,346,254,395,434,220,374,308,
                        220,311,181,274,303,244]
    return tf.to_float(weight_age), tf.to_float(blood_fat_content)
def train(total_loss):
    # 依据计算的总损失训练或调整模型参数
    learning_rate = 0.0000001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)
def evaluate(sess, X, Y):
    # 对训练得到的模型进行评估
    print sess.run(inference([[80., 25.]])) # ~303
    print sess.run(inference([[65., 25.]])) # ~256
    
# 在一个会话对象中启动数据流图，搭建流程
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    
    X, Y = inputs()
    total_loss = loss(X, Y)
    train_op = train(total_loss)
    
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    
    # 实际的训练迭代次数
    training_steps = 1000
    for step in range(training_steps):
        sess.run([train_op])
        # 出于调试和学习的目的，查看损失在训练过程中递减的情况
        if step % 10 == 0:
            print "loss: ", sess.run([total_loss])
            
    evaluate(sess, X, Y)
    
    coord.request_stop()
    coord.join(threads)
    sess.close()

"""
loss:  [7608772.5]
loss:  [5352849.5]
loss:  [5350043.5]
loss:  [5347918.5]
loss:  [5346299.5]
loss:  [5345061.0]
loss:  [5344105.5]
loss:  [5343361.0]
loss:  [5342774.0]
loss:  [5342306.0]
loss:  [5341925.5]
loss:  [5341611.0]
loss:  [5341345.0]
loss:  [5341115.5]
loss:  [5340913.0]
loss:  [5340733.0]
loss:  [5340566.5]
loss:  [5340413.5]
loss:  [5340268.0]
loss:  [5340128.0]
loss:  [5339993.0]
loss:  [5339860.5]
loss:  [5339733.5]
loss:  [5339606.0]
loss:  [5339482.5]
loss:  [5339357.5]
loss:  [5339234.5]
loss:  [5339112.0]
loss:  [5338989.5]
loss:  [5338869.0]
loss:  [5338747.0]
loss:  [5338624.5]
loss:  [5338503.5]
loss:  [5338385.0]
loss:  [5338262.0]
loss:  [5338141.0]
loss:  [5338022.5]
loss:  [5337900.5]
loss:  [5337780.5]
loss:  [5337661.0]
loss:  [5337538.5]
loss:  [5337418.5]
loss:  [5337297.0]
loss:  [5337177.5]
loss:  [5337056.5]
loss:  [5336936.5]
loss:  [5336815.0]
loss:  [5336695.5]
loss:  [5336574.5]
loss:  [5336455.0]
loss:  [5336334.0]
loss:  [5336213.0]
loss:  [5336092.5]
loss:  [5335973.0]
loss:  [5335852.5]
loss:  [5335732.5]
loss:  [5335610.5]
loss:  [5335491.5]
loss:  [5335370.5]
loss:  [5335250.0]
loss:  [5335129.5]
loss:  [5335009.0]
loss:  [5334888.0]
loss:  [5334768.5]
loss:  [5334647.0]
loss:  [5334526.5]
loss:  [5334409.0]
loss:  [5334287.0]
loss:  [5334167.5]
loss:  [5334048.0]
loss:  [5333925.5]
loss:  [5333806.0]
loss:  [5333685.5]
loss:  [5333565.5]
loss:  [5333446.0]
loss:  [5333326.0]
loss:  [5333205.5]
loss:  [5333085.0]
loss:  [5332965.0]
loss:  [5332844.5]
loss:  [5332724.0]
loss:  [5332603.5]
loss:  [5332485.0]
loss:  [5332363.5]
loss:  [5332243.5]
loss:  [5332123.5]
loss:  [5332002.5]
loss:  [5331883.5]
loss:  [5331762.5]
loss:  [5331642.0]
loss:  [5331523.0]
loss:  [5331403.0]
loss:  [5331282.0]
loss:  [5331162.0]
loss:  [5331042.0]
loss:  [5330922.5]
loss:  [5330802.5]
loss:  [5330682.0]
loss:  [5330562.5]
loss:  [5330442.5]
[[ 320.64968872]]
[[ 267.78182983]]
"""
```

### 4.4 对数几率回归

对数几率是为了回答Yes-No类型的问题（如：这封邮件是否为垃圾邮件）的模型。

```
import tensorflow as tf
import os

# w1, w2, ..., wk为模型从训练数据中学习到的参数，或赋予每个变量的“权值”
W = tf.Variable(tf.zeros([5,1]), name="weights")
# b也是一个学习到的参数，这个线性代数中的常量也称为模型的偏置（bias）
b = tf.Variable(0., name="bias")

# 初始化变量和模型参数，定义训练闭环中的运算


def combine_inputs(X):
    return tf.matmul(X, W) + b
def inference(X):
    # 计算推断模型在数据X上的输出，并将结果返回
    return tf.sigmoid(combine_inputs(X))
def loss(X, Y):
    # 依据训练数据X及其期望输出Y计算损失
    return tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=Y, logits=combine_inputs(X)))
def read_csv(batch_size, file_name, record_defaults):
    filename_queue = tf.train.string_input_producer([os.getcwd() + '/data/www_kaggle_com_c_titanic_data/' + file_name])
    reader = tf.TextLineReader(skip_header_lines=1)
    key, value = reader.read(filename_queue)
    
    # decode_csv会将字符串（文本行）转换到具有制定默认值的由张量列构成的元组中
    # 它还会为每一列设置数据类型
    decoded = tf.decode_csv(value, record_defaults=record_defaults)
    
    # 实际上会读取一个文件，并加载一个张量中的batch_size行
    return tf.train.shuffle_batch(decoded, batch_size=batch_size, capacity=batch_size*50, min_after_dequeue=batch_size)
def inputs():
    # 读取或生成训练数据X及其期望输出Y
    passenger_id, survived, pclass, name, sex, age, sibsp, parch, ticket, far, cabin, embarked = \
    read_csv(100, "train.csv",[[0.0],[0.0],[0],[""],[""],[0.0],[0.0],[0.0],[""],[0.0],[""],[""]])
    
    # 转换属性数据
    is_first_class = tf.to_float(tf.equal(pclass, [1]))
    is_second_class = tf.to_float(tf.equal(pclass, [2]))
    is_third_class = tf.to_float(tf.equal(pclass, [3]))
    
    gender = tf.to_float(tf.equal(sex, ["female"]))
    
    # 最终将所有特征排列在一个矩阵中，然后对该矩阵转置，使其每行对应一个样本，每列对应一种特征
    features = tf.transpose(tf.stack([is_first_class, is_second_class, is_third_class, gender, age]))
    survived = tf.reshape(survived, [100, 1])
    return features, survived
def train(total_loss):
    # 依据计算的总损失训练或调整模型参数
    learning_rate = 0.01
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)
def evaluate(sess, X, Y):
    # 对训练得到的模型进行评估
    predicted = tf.cast(inference(X) > 0.5, tf.float32)
    print sess.run(tf.reduce_mean(tf.cast(tf.equal(predicted, Y), tf.float32)))
    
# 在一个会话对象中启动数据流图，搭建流程
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    
    X, Y = inputs()
    total_loss = loss(X, Y)
    train_op = train(total_loss)
    
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    
    # 实际的训练迭代次数
    training_steps = 1000
    for step in range(training_steps):
        sess.run([train_op])
        # 出于调试和学习的目的，查看损失在训练过程中递减的情况
        if step % 10 == 0:
            print "loss: ", sess.run([total_loss])
            
    evaluate(sess, X, Y)
    
    coord.request_stop()
    coord.join(threads)
    sess.close()

"""
loss:  [0.67532045]
loss:  [0.71810073]
loss:  [0.79644454]
loss:  [0.72394025]
loss:  [0.66899329]
loss:  [0.69835836]
loss:  [0.72534424]
loss:  [0.67759621]
loss:  [0.65347588]
loss:  [0.66382843]
loss:  [0.76414263]
loss:  [0.66013122]
loss:  [0.62004519]
loss:  [0.92125052]
loss:  [0.68266261]
loss:  [0.61251819]
loss:  [0.67836243]
loss:  [0.63858169]
loss:  [0.64199418]
loss:  [0.76480895]
loss:  [0.65801513]
loss:  [0.60105777]
loss:  [0.68951064]
loss:  [0.74001259]
loss:  [0.66298646]
loss:  [0.63596451]
loss:  [0.62914956]
loss:  [0.64560241]
loss:  [0.64855391]
loss:  [0.59934586]
loss:  [0.62872136]
loss:  [0.96406555]
loss:  [0.65351182]
loss:  [0.57766515]
loss:  [0.65181214]
loss:  [0.59692121]
loss:  [0.60887361]
loss:  [0.60518587]
loss:  [0.60474974]
loss:  [0.61489969]
loss:  [0.58578169]
loss:  [0.77736437]
loss:  [0.58601081]
loss:  [0.5911864]
loss:  [0.67160326]
loss:  [0.61628783]
loss:  [0.57231557]
loss:  [0.66130179]
loss:  [0.61143208]
loss:  [0.54974848]
loss:  [0.65841734]
loss:  [0.62280494]
loss:  [0.58522499]
loss:  [0.6588369]
loss:  [0.64492279]
loss:  [0.56172615]
loss:  [0.54798192]
loss:  [0.58417988]
loss:  [0.63161713]
loss:  [0.55579841]
loss:  [0.65148944]
loss:  [0.53275305]
loss:  [0.75250292]
loss:  [0.57325572]
loss:  [0.54335988]
loss:  [0.60793871]
loss:  [0.57798791]
loss:  [0.56748545]
loss:  [0.55301166]
loss:  [0.64771217]
loss:  [0.55548257]
loss:  [0.5726195]
loss:  [0.52330786]
loss:  [0.55336457]
loss:  [0.59597546]
loss:  [0.6113373]
loss:  [0.52038378]
loss:  [0.56069934]
loss:  [0.56136423]
loss:  [0.60653317]
loss:  [0.58850175]
loss:  [0.54345769]
loss:  [0.53400582]
loss:  [0.61592114]
loss:  [0.60545367]
loss:  [0.51339042]
loss:  [0.58604193]
loss:  [0.54557133]
loss:  [0.70621771]
loss:  [0.50595647]
loss:  [0.54220909]
loss:  [0.53832078]
loss:  [0.58132058]
loss:  [0.54143113]
loss:  [0.54352576]
loss:  [0.5058822]
loss:  [0.67736113]
loss:  [0.54271412]
loss:  [0.52420175]
loss:  [0.54117113]
0.81
"""
```

### 4.5 softmax分类

和对数几率类似，如果需要回答多个选项的问题，则可以使用softmax，如“你的出生地是波士顿、伦敦还是悉尼”。

可以证明，当类别总数为2时，所得到的输出概率与对数几率回归模型的输出完全相同。

```
import tensorflow as tf
import os

# w1, w2, ..., wk为模型从训练数据中学习到的参数，或赋予每个变量的“权值”
W = tf.Variable(tf.zeros([4,3]), name="weights")
# b也是一个学习到的参数，这个线性代数中的常量也称为模型的偏置（bias）
b = tf.Variable(tf.zeros([3]), name="bias")

# 初始化变量和模型参数，定义训练闭环中的运算

def combine_inputs(X):
    return tf.matmul(X, W) + b
def inference(X):
    # 计算推断模型在数据X上的输出，并将结果返回
    return tf.nn.softmax(combine_inputs(X))
def loss(X, Y):
    # 依据训练数据X及其期望输出Y计算损失
    return tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=Y, logits=combine_inputs(X)))
def read_csv(batch_size, file_name, record_defaults):
    filepath = os.getcwd() + '/data/archive_ics_uci_edu_ml_machine-learning-databases_iris/' + file_name
    print filepath
    filename_queue = tf.train.string_input_producer([filepath])
    reader = tf.TextLineReader(skip_header_lines=0)
    key, value = reader.read(filename_queue)
    
    # decode_csv会将字符串（文本行）转换到具有制定默认值的由张量列构成的元组中
    # 它还会为每一列设置数据类型
    decoded = tf.decode_csv(value, record_defaults=record_defaults)
    
    # 实际上会读取一个文件，并加载一个张量中的batch_size行
    return tf.train.shuffle_batch(decoded, batch_size=batch_size, capacity=batch_size*50, min_after_dequeue=batch_size)
def inputs():
    # 读取或生成训练数据X及其期望输出Y
    sepal_length, sepal_width, petal_length, petal_width, label = \
    read_csv(100, "iris.data", [[0.0], [0.0], [0.0], [0.0], [""]])
    
    # 将类名称转换为从0开始计的类别索引
    label_number = tf.to_int32(tf.argmax(tf.to_int32(tf.stack([
        tf.equal(label, ["Iris-setosa"]),
        tf.equal(label, ["Iris-versicolor"]),
        tf.equal(label, ["Iris-virginica"])
    ])), 0))
    
    # 最终将所有特征排列在一个矩阵中，然后对该矩阵转置，使其每行对应一个样本，每列对应一种特征
    features = tf.transpose(tf.stack([sepal_length, sepal_width, petal_length, petal_width]))
    
    return features, label_number
def train(total_loss):
    # 依据计算的总损失训练或调整模型参数
    learning_rate = 0.01
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)
def evaluate(sess, X, Y):
    # 对训练得到的模型进行评估
    predicted = tf.cast(tf.arg_max(inference(X), 1), tf.int32)
    print sess.run(tf.reduce_mean(tf.cast(tf.equal(predicted, Y), tf.float32)))
    
# 在一个会话对象中启动数据流图，搭建流程
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    
    X, Y = inputs()
    total_loss = loss(X, Y)
    train_op = train(total_loss)
    
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    
    # 实际的训练迭代次数
    training_steps = 1000
    for step in range(training_steps):
        sess.run([train_op])
        # 出于调试和学习的目的，查看损失在训练过程中递减的情况
        if step % 10 == 0:
            print "loss: ", sess.run([total_loss])
            
    evaluate(sess, X, Y)
    
    coord.request_stop()
    coord.join(threads)
    sess.close()

"""
loss:  [1.0898101]
loss:  [1.0255945]
loss:  [0.96274871]
loss:  [0.92197585]
loss:  [0.87096161]
loss:  [0.83135492]
loss:  [0.8084774]
loss:  [0.74558854]
loss:  [0.73596221]
loss:  [0.72645903]
loss:  [0.71248621]
loss:  [0.64435369]
loss:  [0.71710223]
loss:  [0.67891771]
loss:  [0.63535327]
loss:  [0.65278]
loss:  [0.59815222]
loss:  [0.56261504]
loss:  [0.60426992]
loss:  [0.57958722]
loss:  [0.56375986]
loss:  [0.57519257]
loss:  [0.58381337]
loss:  [0.5260874]
loss:  [0.59285313]
loss:  [0.55544424]
loss:  [0.55109018]
loss:  [0.56683725]
loss:  [0.56172943]
loss:  [0.50046748]
loss:  [0.54106611]
loss:  [0.53424037]
loss:  [0.50997531]
loss:  [0.56429338]
loss:  [0.49851722]
loss:  [0.4680905]
loss:  [0.48160231]
loss:  [0.49164033]
loss:  [0.44408408]
loss:  [0.51108491]
loss:  [0.49914119]
loss:  [0.45118889]
loss:  [0.51028806]
loss:  [0.4669376]
loss:  [0.42372391]
loss:  [0.48769584]
loss:  [0.4779554]
loss:  [0.40700623]
loss:  [0.45060676]
loss:  [0.43932101]
loss:  [0.43062064]
loss:  [0.42121479]
loss:  [0.42437348]
loss:  [0.45399034]
loss:  [0.43659493]
loss:  [0.43276969]
loss:  [0.39454204]
loss:  [0.42575085]
loss:  [0.43649933]
loss:  [0.38247386]
loss:  [0.43909293]
loss:  [0.43591797]
loss:  [0.38493904]
loss:  [0.45882562]
loss:  [0.41741362]
loss:  [0.39820695]
loss:  [0.41755006]
loss:  [0.39841416]
loss:  [0.38224483]
loss:  [0.4237037]
loss:  [0.44179505]
loss:  [0.36416036]
loss:  [0.42506337]
loss:  [0.44444671]
loss:  [0.37464827]
loss:  [0.38396451]
loss:  [0.39361459]
loss:  [0.36248261]
loss:  [0.36606964]
loss:  [0.4203414]
loss:  [0.35169998]
loss:  [0.39672509]
loss:  [0.42518175]
loss:  [0.37702134]
loss:  [0.39719743]
loss:  [0.33620185]
loss:  [0.36980641]
loss:  [0.39657184]
loss:  [0.37667787]
loss:  [0.38876054]
loss:  [0.38127685]
loss:  [0.35874954]
loss:  [0.3577871]
loss:  [0.40336663]
loss:  [0.34896478]
loss:  [0.34569588]
loss:  [0.39272159]
loss:  [0.38776734]
loss:  [0.3795453]
loss:  [0.35720593]
0.96
"""
```

### 4.6 多层神经网络

线性回归模型和对数几率回归模型本质上都是单个神经元，它具有以下功能：

- 计算输入特征的加权和。可将偏置视为每个样本中输入特征为1的权重，称之为计算特征的线性组合。
- 然后用一个激活函数（或传递函数）并计算输出。对于线性回归的例子，传递函数为恒等式（即值保持不变），而对数几率回归将sigmoid函数作为传递函数。

类似于异或（XOR）运算的拟合，无法用之前的模型来解决。异或的图形表示，类似一个正方形的两个斜对角的点分别为一组，那么无法用条直线完美地将其分开，因为“异或”函数的输出不是线性可分的。

在多层神经网络中，在输入层和输出层之间增加了一个隐含层（hidden layer），可这样来认识这个新层：它使得网络可以对输入数据提出更多的问题，隐含层中的每个神经元对应一个问题，并依据这些问题的回答最终决定输出的结果。

添加隐含层的作用相当于在数据分布图中允许神经网络绘制一条以上的分隔线。

因此“深度学习”中的“深度”的含义，就是通过添加更多的隐含层，神经网络的层数变得更“深”。这些隐含层之间可采用不同类型的连接，甚至在每层中使用不同的激活函数。

### 4.7 梯度下降法与误差反向传播算法

梯度下降法是一种致力于找到函数极值点的算法。前面介绍过，所谓“学习”便是改进模型参数，以便通过大量训练步骤将损失最小化。有了这个概念，将梯度下降法应用于寻找损失函数的极值点便构成了依据输入数据的模型学习。

当提及损失函数的输入变量时，指的是模型的权值，而非实际数据集的输入特征。一旦给定数据集和所要使用的特征类型，这些输入特征便固定下来，无法进行优化。所以我们所计算的偏导数是相对于推断模型中的每个权值而言的。

反相传播算法是一种高效计算数据流图中梯度的技术。

第三部分 用TensorFlow实现更高级的深度模型
------------------------------

第5章 目标识别与分类
------------------------------

SuperVision团队对图像识别的空前准确性，激发了人们对一种名为卷积神经网络（CNN）的深度学习技术的极大兴趣。CNN可用于能够表示为张量（各个分量与其相关的分量有序排列在一个多维网格中）的任意类型的数据。

### 5.1 卷积神经网络

从技术角度看，卷积神经网络是一种至少包含一个层（tf.nn.conv2d）的神经网络，该层的功能是计算其输入f与一组可配置的卷积核g的卷积，以生成该层的输出。可用一种比较简明的定义描述卷积：卷积的目的是将卷积核（滤波器）应用到某个张量的所有点上，并通过将卷积核在输入张量上滑动而生成经过滤波处理的张量。

CNN通过对多种简单模式分层布局实现复杂模式的匹配。在CNN的语境中，这些模式被称为滤波器或卷积核，而训练的目标是调节这些卷积核的权值，直到它们能够与训练数据精确匹配。要训练这些滤波器，需要将多个不同的层级联，并利用梯度下降法及其变体调节网络权值。

简单的CNN架构通常包含卷积层（tf.nn.conv2d）、非线性变换层（tf.nn.relu）、池化层（tf.nn.max_pool）及全连接层（tf.nn.matmul）。如果没有这些层，模型便很难与复杂的模式匹配，因为网络将被填充过多的信息。一个设计良好的CNN架构会突出那些重要的信息，而将噪声忽略。

![](contents/chapter05/001.png)

```
import tensorflow as tf

image_batch = tf.constant([
    [ # 第1幅图像
        [[1, 255, 0], [2, 255, 0], [3, 255, 0]],
        [[4, 255, 0], [5, 255, 0], [6, 255, 0]]
    ],
    [ # 第2幅图像
        [[7, 0, 255], [8, 0, 255], [9, 0, 255]],
        [[10, 0, 255], [11, 0, 255], [12, 0, 255]]
    ]
])

print image_batch.get_shape()
print image_batch.shape

with tf.Session() as sess:
    print sess.run(image_batch)[0][1][2]
    sess.close()

"""
(2, 2, 3, 3)
(2, 2, 3, 3)
[  6 255   0]
"""
```

其中，`(2, 2, 3, 3)`从左到右分别表示为：图像的数量（2个），图像的高度（2行），图像的宽度（3列），图像的颜色通道数量（3通道）。

### 5.2 卷积

![](contents/chapter05/002.png)

#### 5.2.1 输入和卷积核

卷积核（kernel）是一则重要术语，也称为权值、滤波器、卷积矩阵或模板。由于本任务与计算机视觉相关，使用术语“卷积核”便显得十分有用，因为这意味着将它视为图像卷积核。当用于描述TensorFlow中的相应功能时，使用哪种说法并不存在实际差别。在TensorFlow中，这个参数被命名为filter，相应的权值可从训练中习得。卷积核（filter参数）中不同权值的数量决定了需要学习的卷积核的数量。

```
import tensorflow as tf

input_batch = tf.constant([
    [ # 第一个输入
        [[0.0], [1.0]],
        [[2.0], [3.0]]
    ],
    [ # 第二个输入
        [[2.0], [4.0]],
        [[6.0], [8.0]]
    ]
])

# 卷积核：其作用是返回一个其第1个通道等于原始输入值，第2个通道等于原始输入值两倍的张量
kernel = tf.constant([
    [
        [[1.0, 2.0]]
    ]
])

print input_batch.shape
print kernel.shape

conv2d = tf.nn.conv2d(input_batch, kernel, use_cudnn_on_gpu=False, strides=[1, 1, 1, 1], padding='SAME')

with tf.Session() as sess:
    print sess.run(conv2d)
    sess.close()

"""
(2, 2, 2, 1)
(1, 1, 1, 2)
[[[[  0.   0.]
   [  1.   2.]]

  [[  2.   4.]
   [  3.   6.]]]


 [[[  2.   4.]
   [  4.   8.]]

  [[  6.  12.]
   [  8.  16.]]]]
"""
```

#### 5.2.2 跨度（strides）

图像的高度为6个像素，宽度为6个像素，而深度为1个通道（6x6x1）。卷积核为（3x3x1）。

```
import tensorflow as tf

input_batch = tf.constant([
    [ # 第一个输入(6x6x1)
        [[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]],
        [[0.1], [1.1], [2.1], [3.1], [4.1], [5.1]],
        [[0.2], [1.2], [2.2], [3.2], [4.2], [5.2]],
        [[0.3], [1.3], [2.3], [3.3], [4.3], [5.3]],
        [[0.4], [1.4], [2.4], [3.4], [4.4], [5.4]],
        [[0.5], [1.5], [2.5], [3.5], [4.5], [5.5]]
    ]
])


kernel = tf.constant([ # 卷积核3x3x1
    [[[0.0]], [[0.5]], [[0.0]]],
    [[[0.0]], [[1.0]], [[0.0]]],
    [[[0.0]], [[0.5]], [[0.0]]]
])

print input_batch.shape
print kernel.shape

conv2d = tf.nn.conv2d(input_batch, kernel, use_cudnn_on_gpu=False, strides=[1, 3, 3, 1], padding='SAME')

with tf.Session() as sess:
    print sess.run(conv2d)
    sess.close()

"""
(1, 6, 6, 1)
(3, 3, 1, 1)
[[[[ 2.20000005]
   [ 8.19999981]]

  [[ 2.79999995]
   [ 8.80000019]]]]
"""
```

![](contents/chapter05/003.png)

跨度的意思就是每计算完一次移动所跨越的数量。如果在图像尺寸、卷积核尺寸和strides参数不匹配时，则可采取图像填充边界的方法来处理那些非均匀区域。

设置跨度是一种调整输入张量维数的方法。降维可减少所需的运算量，并可避免创建一些完全重叠的感受域。

#### 5.2.3 边界填充

边界填充是当卷积核与图像尺寸不匹配，但又不允许卷积核跨越图像边界时，会引发一个错误。padding的值可以是下面两种：

- SAME：卷积输出与输入尺寸相同。这里在计算如何跨越图像时，不考虑滤波器的尺寸。选用该设置时，缺失的像素将用0填充，卷积核扫过的像素数将超过图像的实际像素数。

- VALID：在计算卷积核如何在图像上跨越时，需要考虑滤波器的尺寸。这会使卷积核尽量不越过图像的边界。在某些情形下，可能边界也会被填充。

在大多数比较简单的情形下，SAME都是一个不错的选择。当指定跨度参数后，如果输入和卷积核能够很好地工作，则推荐使用VALID。

#### 5.2.4 数据格式

tf.nn.conv2d还有一个参数data_format：该参数可取为“NHWC”或“NCHW”，默认值为“NHWC”，用于指定输入和输出数据的格式。当取默认格式“NHWC”时，数据的存储顺序为`[batch, in_height, in_width, in_channels]`。若该参数为“NCHW”，数据存储顺序为`[batch, in_chinnels, in_height, in_width]`。

#### 5.2.5 深入讨论卷积核

作者用摄影中的滤波器（滤镜）来比喻卷积核（滤波器）在卷积计算中的作用，可以借用不同的滤波器来突出输入数据的特征。

书中介绍了两种简单的滤波器：边缘检测、提升锐度滤波器。

这些卷积核在比较初级的层次上能够与图像中的一些模式匹配。卷积神经网络通过使用从训练过程中学习到的复杂卷积核不但可以匹配边缘，还可以匹配更为复杂的模式。在训练过程中，这些卷积核的初值通车随机设定，随着训练迭代的进行，它们的值会由CNN的学习层自动调整。当CNN训练完成一轮迭代后，它接收一幅图像，并将其与某个卷积核进行卷积，然后依据预测结果与该图像真实标签是否一致，对卷积核中的参数进一步调整。例如，若一幅牧羊犬的照片被CNN模型预测为斗牛犬，则卷积核参数将适当调整以试图更好地匹配牧羊犬图片。

用CNN学习复杂的模式并非只用一个单层卷积就可完成，即使上述示例代码中包含了一个tf.nn.relu层用于准备输出以便可视化，也是不够的。在CNN中，卷积层可多次出现，但通常也会包含其他类型的层。这些层联合起来构成了成功的CNN架构所必须的要素。

### 5.3 常见层

对图像识别和分类任务而言，更常见的情形是使用不同的层类型支持某个卷积层。这些层有助于减少过拟合，并可加速训练过程和降低内存占用率。

#### 5.3.1 卷积层

除了`tf.nn.conv2d`，还有：

1. tf.nn.depthwise_conv2d：当需要将一个卷积层的输出连接到另一个卷积层的输入时，可使用这种卷积。
2. tf.nn.separable_conv2d：它与`tf.nn.conv2d`类似，但并非后者的替代品。对于规模较大的模型，它可不牺牲准确率的前提下实现训练的加速。对于规模较小的模型，它能够快速收敛，但准确率较低。
3. tf.nn.conv2d_transpose：它将一个卷积核应用于一个新的特征图，后者的每一部分都填充了与卷积核相同的值。当该卷积核遍历新图像时，任何重叠的部分都相加在一起。

#### 5.3.2 激活函数

这些函数与其他层的输出联合使用可生成特征图。它们用于对某些运算的结果进行平滑（或微分）。其目标是为神经网络引入非线性。非线性意味着输入和输出的关系是一条曲线，而非直线。曲线能够刻画输入中更为复杂的变化。例如，非线性映射能够描述那些大部分时间值都很小，但在某个单点会周期性地出现极值的输入。为神经网络引入非线性可使其对在数据中发现的复杂模式进行训练。

评价某个激活函数是否有用时，可考虑下列为数不多的几个主要因素：

- 单调的：这样输出便会随着输入的增长而增长，从而使利用梯度下降法寻找局部极值点成为可能。
- 可微分的：以保证该函数定义域内的任意一点上导数都存在，从而使得梯度下降法能够正常使用来自这类激活函数的输出。

1. tf.nn.relu：也叫“斜坡函数”，当输入为非负时，输出将与输入相同；而当输入为负时，输出均为0。
```
import tensorflow as tf
​
features = tf.range(-2, 3)
with tf.Session() as sess:
    print sess.run([features, tf.nn.relu(features)])
    sess.close()
# [array([-2, -1,  0,  1,  2], dtype=int32), array([0, 0, 0, 1, 2], dtype=int32)]
```

2. tf.sigmoid：返回值位于区间[0.0, 1.0]中。
```
import tensorflow as tf
​
features = tf.to_float(tf.range(-1, 3))
with tf.Session() as sess:
    print sess.run([features, tf.sigmoid(features)])
    sess.close()
# [array([-1.,  0.,  1.,  2.], dtype=float32), array([ 0.26894143,  0.5       ,  0.7310586 ,  0.88079703], dtype=float32)]
```

3. tf.tanh：与tf.sigmoid非常接近，返回值位于区间[-1.0, 1.0]中。
```
import tensorflow as tf
​
features = tf.to_float(tf.range(-1, 3))
with tf.Session() as sess:
    print sess.run([features, tf.tanh(features)])
    sess.close()
# [array([-1.,  0.,  1.,  2.], dtype=float32), array([-0.76159418,  0.        ,  0.76159418,  0.96402758], dtype=float32)]
```

4. tf.nn.dropout：当引入少量随机性有助于训练时，这个层会有很好的表现。这种层应该只在训练阶段使用。
```
import tensorflow as tf
​
features = tf.constant([-0.1, 0.0, 0.1, 0.2])
with tf.Session() as sess:
    print sess.run([features, tf.nn.dropout(features, keep_prob=0.5)])
    sess.close()
# [array([-0.1,  0. ,  0.1,  0.2], dtype=float32), array([-0.        ,  0.        ,  0.        ,  0.40000001], dtype=float32)]
```

#### 5.3.3 池化层

池化层能够减少过拟合，并通过减小输入的尺寸来提高性能。它们可用于对输入降采样，但会为后续层保留重要的信息。

1. tf.nn.max_pool：取出最大值，当输入数据的灰度与图像中的重要性相关时，这种池化方式非常有用。
```
import tensorflow as tf

# 输入通常为前一层的输出，而非直接为图像 
batch_size = 1
input_height = 3
input_width = 3
input_channels = 1

layer_input = tf.constant([
    [
        [[1.0], [0.2], [1.5]],
        [[0.1], [1.2], [1.4]],
        [[1.1], [0.4], [0.4]]
    ]
])

# strides 会使用image_height和image_width遍历整个输入
kernel = [batch_size, input_height, input_width, input_channels]
max_pool = tf.nn.max_pool(layer_input, kernel, [1, 1, 1, 1], "VALID")

with tf.Session() as sess:
    print sess.run(max_pool)
    sess.close()

"""
[[[[ 1.5]]]]
"""
```

2. tf.nn.avg_pool：取出平均值，当整个卷积核都非常重要时，若需实现值的缩减，平均池化是非常有用的。
```
import tensorflow as tf

batch_size = 1
input_height = 3
input_width = 3
input_channels = 1

layer_input = tf.constant([
    [
        [[1.0], [1.0], [1.0]],
        [[1.0], [0.5], [0.0]],
        [[0.0], [0.0], [0.0]]
    ]
])

# strides 会使用image_height和image_width遍历整个输入
kernel = [batch_size, input_height, input_width, input_channels]
avg_pool = tf.nn.avg_pool(layer_input, kernel, [1, 1, 1, 1], "VALID")

with tf.Session() as sess:
    print sess.run(avg_pool)
    sess.close()

"""
[[[[ 0.5]]]]
"""
```

#### 5.3.4 归一化

归一化的目标之一在于将输入保持在一个可接受的范围内。例如，将输入归一化到[0.0, 1.0]区间内将使输入中所有可能的分量归一化为一个大于等于0.0且小于等于1.0的值。

```
import tensorflow as tf

layer_input = tf.constant([
    [[[1.]], [[2.]], [[3.]]]
])
lrn = tf.nn.local_response_normalization(layer_input)
with tf.Session() as sess:
    print sess.run([layer_input, lrn])
    sess.close()
"""
[array([[[[ 1.]],

        [[ 2.]],

        [[ 3.]]]], dtype=float32), array([[[[ 0.70710677]],

        [[ 0.89442718]],

        [[ 0.94868326]]]], dtype=float32)]
"""
```

#### 5.3.5 高级层

1. tf.contrib.layers.convolution2d

convolution2d层与tf.nn.conv2d的逻辑相同，但还包括权值初始化、偏置初始化、可训练的变量输出、偏置相加以及添加激活函数的功能。
```
import tensorflow as tf

image_input = tf.constant([
    [
        [[0., 0., 0.], [255., 255., 255.], [254., 0., 0.]],
        [[0., 191., 0.], [3., 108., 233.], [0., 191., 0.]],
        [[254., 0., 0.], [255., 255., 255.], [0., 0., 0.]]
    ]
])

conv2d = tf.contrib.layers.convolution2d(
    image_input,
    num_outputs=4,
    kernel_size=(1,1), # 这里仅有滤波器的高度和宽度
    activation_fn=tf.nn.relu,
    stride=(1, 1), # 对image_batch和input_channels的跨度值
    trainable=True)

# 有必要对在convolution2d的设置中所使用的变量初始化
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print sess.run(conv2d)
    sess.close()

"""
[[[[   0.            0.            0.            0.        ]
   [   0.          216.5531311    36.19777298  143.79277039]
   [   0.          104.80976868   13.69223595  193.31230164]]

  [[   0.           47.72636414    0.            0.        ]
   [   0.           71.72908783   40.20363235    0.        ]
   [   0.           47.72636414    0.            0.        ]]

  [[   0.          104.80976868   13.69223595  193.31230164]
   [   0.          216.5531311    36.19777298  143.79277039]
   [   0.            0.            0.            0.        ]]]]
"""
```

2. tf.contrib.layers.fully_connected
在全连接层中，每个输入和输出之间都存在连接。在许多架构中，这个层都极为常见。对于CNN，最后一层通常都是全连接层。

```
import tensorflow as tf

features = tf.constant([
    [[1.2], [3.4]]
])

fc = tf.contrib.layers.fully_connected(features, num_outputs=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print sess.run([features, fc])
    sess.close()

"""
[array([[[ 1.20000005],
        [ 3.4000001 ]]], dtype=float32), array([[[ 0.60588932,  0.80062568],
        [ 1.71668637,  2.26843953]]], dtype=float32)]
"""
```

3. 输入层

无论是训练还是测试，原始输入都需要传递给输入层。对于目标识别与分类，输入层为tf.nn.conv2d，它负责接收图像。

### 5.4 图像与TensorFlow

#### 5.4.1 加载图像

需要在运算前将图像完整加载到内存中。

```
image_filename = "./images/test.jpg"
filename_queue = tf.train.string_input_producer(
    tf.train.match_filename_once(image_filename)
)
image_reader = tf.WholeFileReader()
_, image_file = image_reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)

sess.run(image)
```

#### 5.4.2 图像格式

1. JPEG与PNG

JPEG图像不会存储任何的alpha通道的信息，但PNG图像会。

使用JPEG图像时，不要进行过于频繁的操作，因为这样会留下一些伪影。

2. TFRecord

为将二进制数据和标签（训练的类别标签）数据存储在同一个文件中，TensorFlow设计了一种内置文件格式，该格式被称为TFRecord，它要求在模型训练之前通过一个预处理步骤将图像转换为TFRecord格式。该格式的最大优点是将每幅输入图像和与之关联的标签放在同一个文件中。

尽管TFRecord文件并非必须，但在使用图像数据时，却是强烈推荐的。

#### 5.4.3 图像操作

1. 裁剪

- `tf.image.central_corp`：将图像中心按比例裁剪出。
- `tf.image.crop_to_bounding_box`：按指定位置大小裁剪出。

2. 边界填充

- `tf.image.pad_to_bounding_box`：对于尺寸过小的图像，该方法会围绕该图像的边界填充一些灰度值为0的像素。
- `tf.image.resize_image_with_corp_or_pad`：对于长宽比不一致的图像，可以使用这个方法来裁剪和边界填充。

3. 翻转

- `tf.image.flip_left_right`：水平翻转
- `tf.image.flip_up_down`：垂直翻转
- `tf.image.random_flip_left_right`：随机水平翻转
- `tf.image.random_flip_up_down`：随机垂直翻转

4. 饱和与平衡

- `tf.image.adjust_brightness`：调整灰度（亮度）
- `tf.image.adjust_contrast`：调整对比度
- `tf.image.adjust_hue`：调整色度（色调）
- `tf.image.adjust_saturation`：调整饱和度

#### 5.4.4 颜色

1. 灰度

- `tf.image.rgb_to_grayscale`：将RGB转化为灰度

2. HSV空间

HSV是色度（Hue）、饱和度（Saturation）和纯度（Value），有时也被称为HSB（Brightness）

- `tf.image.rgb_to_hsv`：将rgb转化为HSV

3. RGB空间

大部分情况下都是用RGB空间，TensorFlow提供了从其他的空间转换过来的方法。

- `tf.image.hsv_to_rbg`：将HSV转化为RGB
- `tf.image.grayscale_to_rbg`：将灰度转化为RGB

4. LAB空间

TensorFlow原生不支持。

Python库python-colormath为LAB和其他本书未提及的颜色空间提供了转换支持。

5. 图像数据类型转换

- `tf.image.convert_image_dtype(image, dtype, saturate=False)`：将图像的数据类型从tf.uint8更改为tf.float的便捷方法。

### 5.5 CNN的实现

本章的网络架构采取了Alex Krizhevsky的AlexNet的简化版本。

#### 5.5.1 Stanford Dogs数据集

下载图像地址：http://vision.stanford.edu/aditya86/ImageNetDogs/



第6章 循环神经网络与自然语言处理
------------------------------

第四部分 其他提示、技术与特性
------------------------------

第7章 产品环境中模型的部署
------------------------------

第8章 辅助函数、代码结构和类
------------------------------

附加信息
------------------------------

1. 1.2版API中和原书中的一些方法不一致，可以参考：https://www.tensorflow.org/api_guides/python/math_ops#Arithmetic_Operators 