Head First Python（中文版）
========================


1 初识Python
-------------

从C语系转过来的科班生，遇到没有{}，没有类型声明，确实有点儿不适应。作者使用了以下例子来进行演示：

```

>>> the_list = ["a1", 2, ["b1", "b2"], 4, "a3", ["b3", ["c1", "c2"]]]
>>> def print_list(the_list):
	for item in the_list:
		if isinstance(item, list):
			print_list(item)
		else:
			print(item)

			
>>> print_list(the_list)
a1
2
b1
b2
4
a3
b3
c1
c2
>>> len(the_list)
6

```

知识点：

- 从命令行或再IDLE中运行Python3.在IDLE中使用Alt+P/N，Mac下用Ctrl+P/N，可以调回上次写的代码。

- 标识符是指数据对象的名字。标识符没有“类型”，不过标识符所指示的数据对象有类型。

- print() BIF会在屏幕上显示一个消息。

- 列表是一个数据集合，数据项之间用逗号分隔，整个列表用中括号包围。列表，在isinstance()的第二个参数是list。

- 列表就像是打了激素的数组。

- 可以用BIF处理列表，另外列表还支持一组列表方法。

- 列表可以存放任意数据，而且数据可以是混合类型。列表还可以包含其他列表。

- 列表可以随需要伸缩。数据使用的所有内存都由Python为你管理。

- Python使用缩进将语句归组（suite）在一起。

- len() BIF会提供某个数据对象的长度，或者统计一个集合中的项数，如列表中的项数

- for循环允许迭代处理一个列表，这通常比使用一个等价的while循环更方便。

- 可以利用if…else…语句在代码中完成判定。

- isinstance() BIF会检查一个标识符是否指示某个指定类型的数据对象。

- 使用def来定义一个定制函数。

- 传言Python起名于[Monty Python](http://baike.baidu.com/view/592799.htm)


2 共享你的代码
-------------

本节主要通过完善上一节的例子，讲述了函数的编写、发布、本地副本、发布到PyPI等特性。

```
>>> this_list = ['a', 'b', ['c', ['d', 'e'], 'f']]
>>> import nester
>>> nester.print_list(this_list)
a
b
c
d
e
f
>>> nester.print_list(this_list, True)
a
b
	c
		d
		e
	f
>>> nester.print_list(this_list, True, 2)
		a
		b
			c
				d
				e
			f
>>> 
```

知识点：

- 模块是一个包含Python代码的文本文件。模块的名称就是文件的名称（不含后缀.py）

- 发布工具允许将模块转换为可共享的包。

```
python3 setup.py register
python3 setup.py sdist upload
```

- setup.py程序提供了模块的元数据，用来构建、安装和上传打包的发布。

```
from distutils.core import setup

setup(
    name = 'nester_volnet',
    version = '1.0.6',
    py_modules = ['nester', 'testnester'],
    author = 'volnet',
    author_email = 'volnet@tom.com',
    url = 'http://volnet.github.io',
    description='A simple printer of nested lists, this version add the testnester.py',
)
```

```
python3 setup.py sdist
sudo python3 setup.py install
```

- 使用import语句可以将模块导入到其他程序中。

```
import nester
```

- Python中的各个模块提供了自己的命名空间，使用module.function()形式调用函数的模块时，要用命名空间名限定函数。

```
nester.print_list(this_list)
```

- 使用import语句的from module import function形式可以从一个模块将函数专门导入到当前命名空间。

```
from nester import print_list
print_list(this_list)
```

- 使用#可以注释掉一行代码，或者为程序增加一个简短的但行注释

- 内置函数（built-in functions, BIF）有自己的命名空间，名为`__builtins__`，这会自动包含在每一个Python程序中。

- range() BIF可以与for结合使用，从而迭代固定次数。

```
for i in range(4):
	print(i)
```

等价于

```
i = 0
while i < 4:
	print(i)
	i = i + 1
```

- 包含end=''作为print() BIF的一个参数会关闭其默认行为（即在输入中自动包含换行）。

- 如果为函数参数提供一个缺省值，这个函数参数就是可选的。

```
def print_list( thislist, level = 0)
```

> 本节示例代码：

> [lastest src samples/nester/](samples/nester/)

> [packages samples/nester.pypi/](samples/nester.pypi/)

> [PyPI url](https://pypi.python.org/pypi/nester_volnet)



3 文件与异常
-------------


4 持久存储
-------------


5 推导数据
-------------


6 定制数据对象
-------------


7 Web开发
-------------


8 移动应用开发
-------------


9 管理你的数据
-------------


10 扩展你的Web应用
----------------


11 处理复杂性
-------------


i 其他
-------------