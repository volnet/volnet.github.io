Head First Python（中文版）
========================

![](contents/wx-cover.png)

> 知道Head First系列图书，怎么也有十年八年了，这是第一次阅读Head First系列，确实和别的图书风格不太一样。

> 一般介绍计算机语言类的图书，都是从语法、规则等入手，按照科班教学的思路，先是变量、然后是循环判断等、再后面是结构、类之类的高级语言特性。

> 而Head First以示例的方式来穿插讲解各种语言要点，同时更强调完成一件事所经历的思考过程，也正因为这种特殊的形式，它并不是很适合作为参考书，而需要顺序阅读。

> 不过我还是尽量从冗长的文章中提炼出语言要点，便于日后复习和参考使用。

> 不过这本书实在是浪费了大量的篇幅用来画图和重复表达，不知道是不是因为出版和稿费的问题。

> 回到Python本身，它的语法确实还需要我去适应，和C风格的语言相比，还是有一些不太一样。但是从语言概念来讲，现在主流的面向对象编程语言所拥有的常用语言特性在Python里面也都有对应。

> Python给人直观的印象则是它拥有大量的社区资源用来完成一些**特定模式**的事情，而且确实现在越来越多的开源框架、书籍都以Python作为主要的示例语言，因此学习它至少是一个很不错的选择。

[原书示例相关下载](http://python.itcarlow.ie/resources.html)

1 初识Python
-------------

作为从C语系转过来的科班生，遇到没有{}，没有类型声明，确实有点儿不适应。作者使用了以下例子来进行演示：

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

- 从`命令行`或在`IDLE`中运行`Python3`.在IDLE中使用Alt+P/N，Mac下用Ctrl+P/N，可以调回上次写的代码。

- 标识符是指数据对象的名字。标识符没有“类型”，不过标识符所指示的数据对象有类型。

- print() BIF会在屏幕上显示一个消息。

- 列表是一个数据集合，数据项之间用逗号分隔，整个列表用中括号包围。示例中在isinstance()的第二个参数是list，代表判断对象是否是list。

- 列表就像是打了激素的数组。

- 可以用BIF处理列表，另外列表还支持一组列表方法。

- 列表可以存放任意数据，而且数据可以是混合类型。列表还可以包含其他列表。

- 列表可以随需要伸缩。数据使用的所有内存都由Python为你管理。

- Python使用缩进将语句归组（suite）在一起。

- len() BIF会提供某个数据对象的长度，或者统计一个集合中的项数，如列表中的项数。

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

- 使用#可以注释掉一行代码，或者为程序增加一个简短的单行注释。

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
def print_list(thislist, level = 0)
```


> 本节示例代码：

> [lastest src samples/chapter02/nester/](samples/chapter02/nester/)

> [packages samples/chapter02/nester.pypi/](samples/chapter02/nester.pypi/)

> [PyPI url](https://pypi.python.org/pypi/nester_volnet)


3 文件与异常
-------------

在本节中，作者用一个文本读取，并进行Split的例子，来说明程序中可能出现的错误，以及如何使用异常处理机制。

不过，读到这里，不知道作者是为了应对这一节的标题，还是真心喜欢异常处理。

在一些其他的语言，如C#中，异常，被认为是比较耗时的行为，一般推荐使用丰富的判断逻辑（if）来处理可预测的错误。但是本节作者更倾向于使用异常以让程序主体占用更多的篇幅。这也表达了该语言更倾向于编写易读、易写、性能要求不高的程序。

```
import os

def getinfo():
    os.getcwd()
    os.chdir("../Documents/")
    #os.chdir("../volnet/volnet.github.io/docs/book/HeadFirstPython/samples/chapter03/")
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

- Python中不可改变的常量列表称为元组（tuple）。一旦将列表数据赋值至一个元组，就不能再改变。元组是不可改变的。

- 数据不符合期望的格式时会出现ValueError。

- 数据无法正常访问时会出现IOError（例如，可能你的数据文件已经被移走或者重命名）。

- help() BIF允许你在IDLE shell中访问Python的文档，比如：help("".split)

- find() 方法会在一个字符串中查找一个特定的子串，找不到则返回-1。

- not关键字将一个条件取反，如`if not x == 1:`，实测也是可以使用`if x != 1:`来表达的。

- try/except语句提供一个异常处理机制，从而保护可能导致运行时错误的某些代码行。

- pass语句就是Python的空语句或null语句，它什么也不做。类似except后面又必需有代码块的时候，就可以使用。


> 本节示例代码：

> [lastest src samples/chapter03/](samples/chapter03/)

> [PyPI url](https://pypi.python.org/pypi/ch03_sketch_volnet)


4 持久存储
-------------

知识点：

- strip()方法可以从字符串去除不想要的空白符。类似于C#中的`" This is ".Trim()` => `"This is"`

- print() BIF的file参数控制将数据发送/保存到哪里，比如`file=sys.stdout`

- finally组总会执行，而不论try/except语句中出现什么异常。

- 会向except组传入一个异常对象，并使用as关键字赋值一个关键字，如：`except IOError as err:`

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

知识点：

- sort()方法可以原地改变列表的顺序。

- sorted() BIF通过提供复制排序可以对几乎任何数据结构排序。

- 向sort()或sorted()传入reverse=True可以降序排列数据。

- 如果有以下代码：

```
new_l = []
for t in old_l:
    new_l.append(len(t))
```

使用列表推导重写这个代码，可以写作：

```
new_l = [len(t) for t in old_l]
```

- 要访问一个列表中的多个数据项，可以使用分片。例如：my_list[3:6]，包含3，但不包含6

```
>>> my_list = [0,1,2,3,4,5,6,7,8]
>>> print(my_list[3:6])
[3, 4, 5]
```

- 这会访问列表中从索引位置3直到（但不包括）索引位置6的列表项。

- 使用set()工厂方法可以创建一个集合


> 本节示例代码：

> [lastest src samples/chapter05/](samples/chapter05/)

> [PyPI url](https://pypi.python.org/pypi/ch05_dealinfo_volnet/)


6 定制数据对象
-------------

```
class MyClass:
    NickName = ''
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def GetName(self):
        return self.Name + '(' + self.NickName + ')'

    def GetAge(self):
        return self.Age

    def AddAge(self, age):
        self.Age += age
        return self.Age

class MyClass2(MyClass):
    def __init__(self, name):
        MyClass.__init__(self, name, 20)

    def AddAge(self, age):
        self.Age += (2 * age)
        return self.Age

obj1 = MyClass('Eric', 18)
obj2 = MyClass2('Volnet')

# Eric 18
print(obj1.GetName() + '-' + str(obj1.GetAge()))
# Volnet 20
print(obj2.GetName() + '-' + str(obj2.GetAge()))

obj1.AddAge(10)
# Eric 18+10=28
print(obj1.GetName() + '-' + str(obj1.GetAge()))

obj2.AddAge(10)
# Volnet 20+2*10=40
print(obj2.GetName() + '-' + str(obj2.GetAge()))

obj1.Name = 'Eric Kung'
obj1.NickName = 'volnet'
# Eric Kung(volnet) 18+10=28
print(obj1.GetName() + '-' + str(obj1.GetAge()))
# Volnet 20
print(obj2.GetName() + '-' + str(obj2.GetAge()))
```

知识点：

- dict()工厂函数或使用{}可以创建一个空字典。

- 要访问一个名为person的字典中与键Name关联的值，可以使用我们熟悉的中括号记忆法：person["Name"]

```
>>> person = { "Name":"volnet" }
>>> person["Name"]
'volnet'
```

- 类似于列表和集合，Python的字典会随着新数据增加到这个数据结构中而动态扩大。

- 可以先创建一个空字典：`new_d = {}` 或 `new_d = dict()`然后增加数据`d["Name"] = "Eric Idle"`来填充字典，或者也可以一次完成以上的全部工作：`new_d = {'Name':'Eric Idle'}`

- 可以用class关键字定义一个类。

```
>>> class Person:
	Name = 'volnet'

	
>>> a = Person()
>>> a.Name
'volnet'
```

- 类方法（代码）与函数的定义基本相同，也就是说，要用def关键字定义。

- 类属性（数据）就像是对象实例中的变量。

- 可以在类中定义__init__()方法来初始化对象实例。

- 类中定义的每个方法都必须提供self作为第一个参数。

- 类中的每个属性前面都必须有self，从而将数据与其实例关联。

- 类可以从零开始构建，也可以从Python的内置类或从其他定制类继承。

- 类可以放在一个Python模块中，并上传到PyPI。


> 本节示例代码：

> [lastest src samples/chapter06/](samples/chapter06/)


7 Web开发
-------------

知识点：

- 模型-视图-控制器（Model-View-Controller）模式允许你采用一种可维护的方式设计和构建一个Web应用。

- 模型存储Web应用的数据。

- 视图显示Web应用的用户界面。

- 控制器将所有代码与编程逻辑“粘合”在一起。

- 标准库string模块包括一个名为Template的类，它支持简单的字符串替换。

- 标准库http.server模块可以用来在Python中建立一个简单的Web服务器。

- 标准库CGI模块对编写CGI脚本提供了支持。

- 标准库glob模块非常适合处理文件名列表。

- 在Linux和Mac OS X上可以使用`chmod +x`命令设置可执行权限位。

- 启用标准库cgitb模块时，允许在浏览器中查看CGI编码错误。

- CGI代码中可以使用cgitb.enable()打开CGI跟踪。

- 可以使用cgi.FieldStorage()访问作为Web请求一部分发送给Web服务器的数据，数据将作为一个Python字典。


> 本节示例代码：

> [lastest src samples/chapter07/](samples/chapter07/)


8 移动应用开发
-------------

本节所涉及的SL4A已经从[code.google.com](https://code.google.com/p/android-scripting/)迁移到[Github](https://github.com/damonkohler/sl4a)了

因Android模拟器的问题，本节未实现在Android手机上的调试。

知识点：

- JSON库模块允许将Python的内置类型转换为基于文本的JSON数据交换格式。

- 使用`json.dumps()`可以创建一个Python类型的字符串版本。

- 使用`json.loads()`可以从一个JSON字符串创建一个Python类型。

- 如果数据使用JSON发送，需要将`Content-Type`设置为`application/json`。

- urllib和urllib2库模块（都在Python2中提供）可以用来从一个程序向Web服务器发送编码的数据（使用urlencode()和urlopen()函数）。

- sys模块提供了sys.stdin、sys.stdout和sys.stderr输入流。


> 本节示例代码：

> [lastest src samples/chapter08/](samples/chapter08/)

> 原文中使用SL4A在Android上用Python2进行http调用，因此使用的urlopen和urlencode与Python3中不太一样。而这里我使用Python3进行client调用，因此代码上略有不同。


9 管理你的数据
-------------

```
import sqlite3

# create database 

conn = sqlite3.connect('coachdata.sqlite')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE athletes(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    dob DATE NOT NULL
)""")
cursor.execute("""CREATE TABLE timing_data(
    athlete_id INTEGER NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY(athlete_id) REFERENCES athletes
)""")

conn.commit()
conn.close()

# init database

conn = sqlite3.connect('coachdata.sqlite')
cursor = conn.cursor()

import glob
import athletemodel

data_files = glob.glob('../data/*.txt')
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob

    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    conn.commit()

conn.close()

```

知识点：

- 标准库cgi模块中的`fieldStorage()`方法允许从CGI脚本访问发送至Web服务器的数据。

- 标准OS库包含一个environ字典，可以很方便地访问程序的环境设置。

```
#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os
import time
import sys

addr = os.environ["REMOTE_ADDR"]
host = os.environ["REMOTE_HOST"]
serverport = os.environ["SERVER_PORT"]
method = os.environ["REQUEST_METHOD"]

cur_time = time.asctime(time.localtime())

print(os.environ, file=sys.stderr)
print('host = ' + host + ', addr = ' + addr + ', serverport = ' + serverport + ', cur_time = ' + cur_time + ', method = ' + method, file=sys.stderr)

```

- SQLite数据库系统作为sqlite3标准库包含在Python中。

- connect()方法可以建立与数据库文件的一个连接。

- cursor()方法允许通过一个已有的连接与数据库通信。

- execute()方法允许通过一个已有的连接向数据库发送一个SQL查询。

- commit()方法使之前对数据库所做的修改永久保留。

- rollback()方法取消对数据做出的所有未完成的修改。

- close()方法关闭与数据库的一个现有连接。

- “?”占位符允许在Python代码中为SQL语句指定参数。


> 本节示例代码：

> [lastest src samples/chapter09/](samples/chapter09/)


10 扩展你的Web应用
----------------

因Google App Engine（GAE）已经升级为[Google Cloud Platform](https://cloud.google.com/)，因此本节涉及的内容可能不再适用。

知识点：

- 每个App Engine Web应用必须有一个名为app.yaml的配置文件。

- 可以使用GAE Launcher启动、停止、监视、测试、上传和部署你的Web应用。

- App Engine的模板技术建立在Django项目所用模板技术基础之上。

- App Engine还可以使用Django的表单验证框架。

- 可以使用self.response对象来构造一个GAE Web响应。

- 可以使用self.request对象来访问一个GAE Web应用的表单数据。

- 响应一个GET请求时，要在一个get()方法中实现必要的功能。

- 响应一个POST请求时，要在一个post()方法实现必要的功能。

- 使用put()方法将数据存储在App Engine datastore中。

11 处理复杂性
-------------

知识点：

- input() BIF允许为用户提供提示语并接收输入。

```
>>> userinput = input('Please enter a word:')
Please enter a word:Hi
>>> userinput
'Hi'
```

- 如果你在使用Python2而且需要input()函数，那么可以使用raw_input()函数。

- 可以结合Python内置的列表、集合和字典构造复杂的数据结构。

- time模块作为标准库的一部分，包含了大量函数可以完成时间格式之间的转换。

- “条件”列表推导尾部包括一个“if”语句，允许在推导运行时控制哪些项可以增加到新的列表中。

- 列表推导可以重写为一个“for”循环。

```
>>> results = []
>>> mylist = [1,2,3,4,5,6,7]
>>> for item in mylist:
	if item > 3:
		results.append(item)

		
>>> results
[4, 5, 6, 7]
```
等价于
```
>>> mylist = [1,2,3,4,5,6,7]
>>> results = [item for item in mylist if item > 3]
>>> results
[4, 5, 6, 7]
```

i 其他
-------------

- 1.使用一个“专业”的IDE

作者推荐[WingWare Python IDE](https://wingware.com/)作为专业的Python IDE工具。

- 2.处理作用域

以下代码将产生UnboundLocalError错误。
```
name = 'Head First Python'
def what_happen_here():

	print('1.' + name)
	
	name = name + ' is a great book!'
	
	print('2.' + name)

what_happen_here()
print('3.' + name)

"""
Traceback (most recent call last):
  File "/Users/volnet/volnet.github.io/docs/book/HeadFirstPython/samples/chapter12/test-i2-1.py", line 10, in <module>
    what_happen_here()
  File "/Users/volnet/volnet.github.io/docs/book/HeadFirstPython/samples/chapter12/test-i2-1.py", line 4, in what_happen_here
    print('1.' + name)
UnboundLocalError: local variable 'name' referenced before assignment
>>> 
"""
```
以下代码使用了global关键字修复了作用域问题：
```
name = 'Head First Python'
def what_happen_here():
    print('1.' + name)
    global name
    name = name + ' is a great book!'
    print('2.' + name)
what_happen_here()
print('3.' + name)

"""
1.Head First Python
2.Head First Python is a great book!
3.Head First Python is a great book!
"""
```
在全局范围定义的变量，在私有方法中，是可以读取的，但是**不能修改**。
所以`print('1.' + name)`的方法可以正确执行。但是后面的`name = name + ' is a great book!'`方法则会失败。

使用`global`关键字明确地表明接下来要访问和修改的是全局变量，而后就可以正确执行赋值语句了。这也避免了无意间修改了全局变量的值。

- 3.测试

Python的标准测试框架分为两种：`unittest`和`doctest`

- 4.高级语言特性

Python还支持下面这些语言特性（不止以下这些）：
    
    - 匿名函数

    - 生成器

    - 定义异常

    - 函数修饰符

    - 元类

- 5.正则表达式

- 6.关于Web框架

常见的适用于Python的Web框架有：
[Django](https://www.djangoproject.com/)、
[Zope](http://docs.zope.org/zopetoolkit/)、
[TurboGears](http://turbogears.org/)、
[Web2py](http://www.web2py.com/)和
[Pylons](http://www.pylonsproject.org/)

- 7.对象关系映射工具和NoSQL

- 8.GUI编程

下面这些技术可以构建基于GUI的Python应用：tkinter、PyGTK、PyKDE、wxPython和PyQT

- 9.要避免的问题

Python使用一种称为全局解释器锁（Global Interpreter Lock，GIL）的技术来实现。它强制实行这样一个限制，要求Python只能在一个解释器进程中运行，即使有多个处理器可用。

对于你来说，这意味着，如果你的程序使用了线程，尽管它的设计和实现都很棒，但是即使有多个处理器这个程序也不会运行得更快，因为它根本无法使用多个处理器。你的线程应用会串行运行，而且在很多情况下，甚至比没有用线程开发同样的功能时慢得多。

要点：除非去除GIL限制（如果真的能去除）……否则不要在Python线程中使用线程。

- 10.其他Python书

    1. 《[Dive Into Python 3](https://www.amazon.cn/Dive-Into-Python-3-Pilgrim-Mark/dp/1430224150/ref=sr_1_1?ie=UTF8&qid=1472223137&sr=8-1&keywords=dive+into+python+3)》

    2. 《[Python学习手册（原书第4版）](https://www.amazon.cn/Python学习手册-MarkLutz/dp/B00H6X6KH6/ref=sr_1_8?ie=UTF8&qid=1472223220&sr=8-8&keywords=python)》

    3. 《[Python 3程序开发指南（第2版 修订版）](https://www.amazon.cn/Python-3程序开发指南-美-萨默菲尔德/dp/B00U0UURS0/ref=sr_1_63?ie=UTF8&qid=1472223254&sr=8-63&keywords=python)》

    4. 《[Python for Unix and Linux Systems Administration](https://www.amazon.cn/Python-for-Unix-and-Linux-Systems-Administration-Jones-Jeremy/dp/0596515820/ref=sr_1_1?ie=UTF8&qid=1472223536&sr=8-1&keywords=python+for+unix)》

    5. 《[Python Essential Reference (4th Edition)](https://www.amazon.cn/Python-Essential-Reference-Beazley-David/dp/0672329786/ref=sr_1_1?ie=UTF8&qid=1472223585&sr=8-1&keywords=python+essential+reference)》

> 本节示例代码：

> [lastest src samples/chapter12/](samples/chapter12/)