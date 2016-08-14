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

```
"""This is the "standard" way to include a multiple-line comment in your code."""

# This is a single line comment

def print_list(the_list, indent = False, level = 0):
	for item in the_list:
		if isinstance(item, list):
			print_list(item, indent, level + 1)
		else:
			if indent:
				for i in range(level):
					print("\t", end="")
			print(item)
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

在第三节中，作者用一个文本读取，并进行Split的例子，来说明程序中可能出现的错误，以及如何使用异常处理机制。

不过，读到这里，不知道作者是为了应对这一节的标题，还是真心喜欢异常处理。

在一些其他的语言，如C#中，异常，被认为是比较耗时的行为，一般推荐使用丰富的判断逻辑（if）来处理可预测的错误。但是本节作者更倾向于使用异常以让程序主体占用更多的篇幅。

```
import os

def getinfo():
    os.getcwd()
    os.chdir("../Documents/")
    #os.chdir("../Dropbox/Documents/个人/volnet.github.io/docs/book/HeadFirstPython/samples/chapter03/")
    os.getcwd()

    try:
        data = open('sketch.txt')
        print(data.readline(), end='')
        print(data.readline(), end='')

        print("---------")

        data.seek(0)
        """
        # use if to deal with the error
        for each_line in data:
            if not each_line.find(":") == -1 :
                (role, line_spoken) = each_line.split(":", 1)
                print(role, end = '')
                print(" said: ", end = '')
                print(line_spoken, end='')
        """

        # use except to deal with the error
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                print(role, end = '')
                print(" said: ", end = '')
                print(line_spoken, end='')
            except ValueError:
                pass

        data.close()

    except IOError:
        print("The data file is missing!")
```

知识点：

- 使用open() BIF打开一个磁盘文件，创建一个迭代器从文件读取数据，一次读取一个数据行。

- readline()方法从一个打开的文件读取一行数据。

- seek()方法可以用来将文件“退回”到起始位置。

- close()方法关闭一个之前打开的文件。

- split()方法可以将一个字符串分解为一个子串列表。第二个参数maxsplit代表最多迭代几个分隔符，比如写1，则代表将文本分成两段。另外返回值是个tuple，用括号(p1, p2)，里面的内容一旦创建就不能修改，这点是与列表[p1, p2]最大的区别。

- Python中不可改变的常量列表称为元组（tuple）。一旦将列表数据赋值至一个元祖，就不能再改变。元组是不可改变的。

- 数据不符合期望的格式时会出现ValueError。

- 数据无法正常访问时会出现IOError（例如，可能你的数据文件已经被移走或者重命名）。

- help() BIF允许你再IDLE shell中访问Python的文档，比如：help("".split)

- find() 方法会在一个字符串中查找一个特定的子串，找不到则返回-1。

- not关键字将一个条件取反，如`if not x == 1:`，实测也是可以使用`if x != 1:`来表达的。

- try/except语句提供一个异常处理机制，从而保护可能导致运行时错误的某些代码行。

- pass语句就是Python的空语句或null语句，它什么也不做。类似except后面又必需有代码块的时候，就可以使用。

> 本节示例代码：

> [lastest src samples/chapter03/](samples/chapter03/)

> [PyPI url](https://pypi.python.org/pypi/ch03_sketch_volnet)

4 持久存储
-------------

- strip()方法可以从字符串去除不想要的空白符。类似于C#中的`" This is ".Trim()` => `"This is"`

- print() BIF的file参数控制将数据发送/保存到哪里，比如`file=sys.stdout`

- finally组总会执行，而不论try/except语句中出现什么异常。

- 会向except组传入一个异常对象，并使用as关键字赋至一个关键字，如：`except IOError as err:`

- str() BIF可以用来访问任何数据对象（支持串转换）的串表示。如：

```
except IOError as err:
    print(str(err))
```

- locals() BIF返回当前作用域中的变量集合。

```
try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError as err:
    print('File error' + str(err))
finally:
    if 'data' in locals():
        data.close()
```

- in操作符用于检查成员关系，如：`if 'data' in locals():`

- “+”操作符用于字符串时将联接两个字符串，用于数字时则会将两个数相加。

- with语句会自动处理所有已打开文件的关闭工作，即使出现异常也不例外。with语句也使用as关键字。[语法](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
同时还可以使用逗号语法。

```
with open('data1.txt', 'r') as data1, open('data2.txt', 'w') as data2:
    print(data1.read(), file=data2)
```

- sys.stdout是Python中所谓的“标准输出”，可以从标准库的sys模块访问。

- 标准库的pickle模块允许你容易而高效地将Python数据对象保存到磁盘以及从磁盘恢复。

- pickle.dump()函数将数据保存到磁盘。

- pickle.load()函数从磁盘恢复数据。


> 本节示例代码：

> [lastest src samples/chapter04/](samples/chapter04/)

> [PyPI url](https://pypi.python.org/pypi/ch04_sketch_volnet)

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