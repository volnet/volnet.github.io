Python语言及其应用
============================================

Introducing Python

[美]Bill Lubanovic著
丁嘉瑞 梁杰 禹常隆 译

![](contents/cover.png)

前言
--------------------------------------------

介绍了本书的每一章节的主体内容。总体来说，这本书是面向初学者的读物。

第1章 Python初探
--------------------------------------------

### 1.1 真实世界中的Python

Python无处不在，从命令行、图形界面、移动设备、甚至是云都存在。既可以写简单的代码，也可以写复杂的产品。

### 1.2 Python与其他语言

- shell：超过百行后扩展性差，比其他语言速度慢
- C/C++：难学，很多细节需要自己处理，因为太难了所以容易引起问题，重视性能
- Java：比C/C++简单容易，但是代码更长，也有更多限制
- Perl：扩展丰富，适应面广，但是语法难用
- Ruby：和Python很多场景相同，非常类似
- PHP：很少用于Web以外的领域，语言本身有许多缺陷

静态语言：语言中的变量不能改变类型，需要告诉计算机它的类型（会使用多少内存），然后被编译成机器语言来执行。

动态语言：由解释器来解释类型是什么类型，比如x=5，那么x就是整形。但相比静态语言也会更慢。

### 1.3 为什么选择Python

- 可读性强
- 语法简洁
- 流行
- 免费
- 运行环境多样
- 标准库很有用
- 广受喜欢

### 1.4 何时不应该使用Python

追求性能的时候，可以用C/C++/Java来替代，但是可以通过优化算法、减少网络延迟提高CPU利用率、用C扩展、不断优化/升级解释器、更换为Go语言等。

### 1.5 Python 2与Python 3

Python 2和Python 3不兼容，用后者编写的程序无法很好运行于前者的系统中。

但二者差别不大，本书以Python 3为主。

### 1.6 安装Python

参考附录D。

### 1.7 运行Python

可以使用：

- 交互式解释器：安装后自带
- 保存成文件用`python`命令执行

### 1.8 禅定一刻

在Python中输入`import this`会有彩蛋：

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### 1.9 练习

无

第2章 Python基本元素：数字、字符串和变量
--------------------------------------------

### 2.1 变量、名字和对象

Python中布尔值、整型、浮点数、字符串、甚至大型数据结构、函数以及程序，都是以对象（object）的形式存在的。

它是强类型的（strongly typed），你永远无法修改一个已有对象的类型，即使它包含的值是可变的。

所谓变量就是在程序中为了方便地引用内存中的值而为它取的名称。

Python中的变量有一个非常重要的性质：它仅仅是一个名字。赋值操作并不会实际复制值，它只是为数据对象取个相关的名字。名字是对对象的引用而不是对象本身。你可以把名字想象成贴在盒子上的标签。

`type( thing )`可以查看对象的类型。

```
a = 10
print(type(a))

a = 10.1
print(type(a))

<class 'int'>
<class 'float'>
```

### 2.2 数字

`/`是浮点数除法，7/2=3.5，即便可以整除，也是浮点型，如a=10/5，那么a是浮点型。

`//`是整数除法，7//2=3

`**` 是幂，3**4=81（3的4次方）

#### 2.2.1 整数

`+123` 和 `123` 等价，都表示正整数。

`9 % 5` 可以得到余数`4`，用 `divmod(9, 5)` 可以同时得到商和余数`(1, 4)`。

#### 2.2.2 优先级

可以使用优先级表来判断优先级，也可以使用括号来使它更明确。

#### 2.2.3 基数

这里是指不同的进制：

- 不带前缀代表十进制，10
- 0b或者0B前缀代表二进制，0b10 => 2
- 0o或者0O前缀代表八进制，0o10 => 8
- 0x或者0X前缀代表十六进制，0x10 => 16

#### 2.2.4 类型转换

使用`int(xxx)`可以进行类型转换，也可以转换字符串，但字符串必须是一个整数，不接受小数点和指数的字符串。

不同类型的数字之间进行运算的时候，会完成自动类型转换。

#### 2.2.5 一个int有多大

python2中int是32位，long是64位，python3中没有long类型，int的范围可以是任意大小甚至超过64位。

#### 2.2.6 浮点数

可以使用`float(xxx)`将其他数字类型转换为浮点型。如果待转换的类型是字符串，那么字符串的内容可以是数字、正负号、小数点、指数及指数的前缀e。

#### 2.2.7 数学函数

附录C会包含数学函数。

### 2.3 字符串

Python的字符串不可改变，但可以复制。

#### 2.3.1 使用引号创建

可以使用单引号或双引号。可以使用三个引号来建立多行文本。

#### 2.3.2 使用str()进行类型转换

可以将其他类型转换为字符串类型

#### 2.3.3 使用\转义

`\t`、`\n`、`\\`、`\"`等都是常见的转义字符。

#### 2.3.4 使用+拼接

可以将多个字符串用`+`拼接，不会自动在中间添加空格。

但是使用print(a,b,c)，默认则会在输出中，每个变量之间添加空格，并在最后添加换行符。

#### 2.3.5 使用*复制

能把一个字符串复制多份，如`a='Na'*4`，那么`a=NaNaNaNa`。

#### 2.3.6 使用[]提取字符

可以用[x]来提取字符串中的字符，其中x是偏移量。

无法直接修改字符串中的字符，比如`a[2]='H'`，需要用`x=a.replace(...)`或者`x=a[:3] + '3' + a[4:]`。

#### 2.3.7 使用[start:end:step]分片

一个极端的例子：

```
a = '123456789'
b = a[-7:-2:2]
print(b)
357
In [24]:

a = '123456789'
b = a[-2:-7:-2]
print(b)
864
```

- 每个参数都可以是正数和负数，正数从左往右，负数从右往左。
- step为负数，则会从右往左，所以start应该是大于end的（正常是小于）。

#### 2.3.8 使用len()获得长度

空字符串的长度为0。

#### 2.3.9 使用split()分割

split如果传递参数，则按参数进行分割，如果不传参数，则使用空白字符分割，包括换行符、空格、制表符。

#### 2.3.10 使用join()合并

`'\n'.join(['a', 'b', 'c'])`，其中join前面的是连字符。

#### 2.3.11 熟悉字符串

- startswith(x)：是否开始于x
- endswith(x)：是否结束于x
- find(x)：从左往右查x
- rfind(x)：从右往左查x
- count(x)：x出现次数
- x.isalnum()：x中是否都是字母或数字

#### 2.3.12 大小写与对齐方式

- x.strip('.')：去掉行尾的字符'.'（可以替换成别的）
- x.capitalize()：让字符串首字母变成大写
- x.title()：让所有单词的开头字母变成大写
- x.upper()：让所有字母都变成大写
- x.lower()：让所有字母都变成小写
- x.swapcase()：让所有字母的大小写转换
- x.center(N)：在N个字符中居中
- x.ljust(N)：在N个字符中居左
- x.rjust(N)：在N个字符中居右

#### 2.3.13 使用replace()替换

x.replace('a ', 'a famous ', 100)：把所有`a `替换成`a famous `，只替换前100个。

#### 2.3.14 更多关于字符串的内容

https://docs.python.org/3/library/stdtypes.html#string-methods 可以查到更多的方法。

### 2.4 练习

无

第3章 Python容器：列表、元祖、字典与集合
--------------------------------------------

### 3.1 列表和元组

元组是不可变的，一旦赋值就再也无法修改。

列表是可变的，可以随意地插入或删除其中的元素。

### 3.2 列表

#### 3.2.1 使用[]或list()创建列表

列表是有顺序的、其中的值是允许重复的。

如果不在乎顺序，建议使用集合（set）。

#### 3.2.2 使用list()将其他数据类型转换成列表

可以将字符串、元组转换成列表。也可以用字符串的`split`方法将其分割成列表。

#### 3.2.3 使用[offset]获取元素

offset从0开始，从左往右计数。

offset从-1开始，从右往左计数。

#### 3.2.4 包含列表的列表

列表可以包含各种类型的元素，也可以多级嵌套。

#### 3.2.5 使用[offset]修改元素

可以用`a[offset]=b`修改元素，元素的类型和之前的可以不同。

不能用该方法修改字符串。

#### 3.2.6 指定范围并使用切片提取元素

可以通过切片提取出子列表。

可以正向提取，也可以逆向提取。

```
marxes = ['Groucho', 'Chico', 'Harpo']

'''从指定位置0开始2（2-0）个元素'''
print(marxes[0:2]) 

'''从指定位置2开始1（3-2）个元素'''
print(marxes[2:3]) 

'''从列表最左端开始2（偏移量为2，不含2）个元素'''
print(marxes[::2]) 

'''从右往左2（从右往左第2个元素开始，直到最左的元素结束）个元素'''
print(marxes[::-2]) 

'''列表逆序（从右往左第1个元素开始，直到最左的元素结束）'''
print(marxes[::-1]) 

['Groucho', 'Chico']
['Harpo']
['Groucho', 'Harpo']
['Harpo', 'Groucho']
['Harpo', 'Chico', 'Groucho']
```

#### 3.2.7 使用append()添加元素至尾部

```
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

['Groucho', 'Chico', 'Harpo', 'Zeppo']
```

#### 3.2.8 使用extend()或+=合并列表

```
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
```

#### 3.2.9 使用insert()在指定位置插入元素

```
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(3, 'Gummo')
print(marxes)

marxes.insert(10, 'Karl')
print(marxes)

['Groucho', 'Chico', 'Harpo', 'Gummo']
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
```

#### 3.2.10 使用del删除指定位置的元素

del是Python语句而不是列表方法——无法通过marxes[-2].del()调用。

```
marxes = ['Groucho', 'Chico', 'Harpo']
del marxes[2]
print(marxes)

['Groucho', 'Chico']
```

#### 3.2.11 使用remove()删除具有指定值的元素

```
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
print(marxes)

['Groucho', 'Chico', 'Harpo', 'Zeppo']
```

#### 3.2.12 使用pop()获取并删除指定位置的元素

pop()等价于pop(-1)。

```
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']

a = marxes.pop()
print(a)
print(marxes)

b = marxes.pop(1)
print(b)
print(marxes)

Zeppo
['Groucho', 'Chico', 'Harpo', 'Gummo']
Chico
['Groucho', 'Harpo', 'Gummo']
```

#### 3.2.13 使用index()查询具有特定值的元素位置

```
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print(marxes.index('Harpo'))

2
```

#### 3.2.14 使用in判断值是否存在

```
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print('Groucho' in marxes)
if('Groucho' in marxes):
    print('A')
else:
    print('B')

True
A
```

#### 3.2.15 使用count()记录特定值出现的次数

```
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print(marxes.count('Groucho'))

print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

1
0
3
```

#### 3.2.16 使用join转换为字符串

`join`是字符串方法，因此是`'*'.join(['a', 'b', 'c'])`。

```
friends = ['Harry', 'Hermione']
separator = ' * '
joined = separator.join(friends)
print(joined)

friends01 = joined.split(separator)
print(friends01)

Harry * Hermione
['Harry', 'Hermione']
```

#### 3.2.17 使用sort()重新排列元素

- 列表方法sort()会对原列表进行排序，改变原列表内容；
- 通用函数sorted()则会返回排好序的列表副本，原列表内容不变。

```
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
sorted_marxes = sorted(marxes)

print(sorted_marxes)
print(marxes)

marxes.sort()
print(sorted_marxes)

['Chico', 'Groucho', 'Gummo', 'Harpo', 'Zeppo']
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
['Chico', 'Groucho', 'Gummo', 'Harpo', 'Zeppo']
```

#### 3.2.18 使用len()获取长度

```
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print(len(marxes))

5
```

#### 3.2.19 使用=赋值，使用copy()复制

复制一个列表，可以用下面三种方法：

- 列表copy()函数
- list()转换函数
- 列表分片[:]

```
a = [1,2,3]
b = a
a[0] = 'hello'
print(a)
print(b)

c = a.copy()
d = list(a)
e = a[:]
a[1] = 'world'
print(a)
print(c)
print(d)
print(e)

['hello', 2, 3]
['hello', 2, 3]
['hello', 'world', 3]
['hello', 2, 3]
['hello', 2, 3]
['hello', 2, 3]
```

### 3.3 元组

#### 3.3.1 使用()创建元组

- 空元组：`empty_tuple = ()`
- 1个元素元组，需要以逗号结尾。`one_marx='Groucho',`
- 多个元素元组，最后逗号可以省略。`marx_tuple='Groucho', 'Chico', 'Harpo'`
- 括号是可有可无的。`marx_tuple=('Groucho', 'Chico', 'Harpo')`
- 元组解包：可以一次将多个值复制给多个对象，每个对象按顺序获得一个值。`a,b,c=marx_tuple`，其中`a='Groucho'`、`b='Chico'`、`c='Harpo'`。
- 利用元组解包可以巧妙进行多个变量交换。`password, icecream = icecream, password`
- `tuple()`函数可以用其他类型的数据来创建元组。

#### 3.3.2 元组与列表

列表比元组灵活，但元组仍然有用，原因在于：

- 元组占用的空间较小
- 不会意外修改元组的值
- 可以将元组用作字典的键
- 命名元组可以作为对象的替代
- 函数的参数是以元组形式传递的

### 3.4 字典

字典（dictionary）与列表类似，但是它通过键来访问元素。

它可以用任意不可变类型作为键，如字符串、布尔型、整形、浮点型、元组，以及一些其他不可变类型。

字典可以增加、删除或修改键值对。

#### 3.4.1 使用{}创建字典

```
empty_dict = {}
print(empty_dict)

word_dict = {
    "hello": "world",
    "good": "luck",
}
print(word_dict)

{}
{'hello': 'world', 'good': 'luck'}
```

字典的最后一个元素后面可以添加逗号。

#### 3.4.2 使用dict()转换为字典

可以转换双值子序列的序列为字典：

列表：
```
lol = [['a','b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

lol = [['a','b'], ['e', 'f'], ['c', 'd']]
print(dict(lol))

{'a': 'b', 'c': 'd', 'e': 'f'}
{'a': 'b', 'e': 'f', 'c': 'd'}
```

包含双值元组的列表：
```
lot = [('a','b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))

{'a': 'b', 'c': 'd', 'e': 'f'}
```

包含双值列表的元组：

```
tol = (['a','b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

{'a': 'b', 'c': 'd', 'e': 'f'}
```

双字符串的字符串组成的列表：（如果字符中包含3个字母，长度必须为2，则会出现异常）

```
los = ['ab', 'cd', 'ef']
print(dict(los))

{'a': 'b', 'c': 'd', 'e': 'f'}
```

双字符的字符串组成的元组：（如果字符中包含3个字母，长度必须为2，则会出现异常）

```
tos = ('ab', 'cd', 'ef')
print(dict(tos))

{'a': 'b', 'c': 'd', 'e': 'f'}
```

#### 3.4.3 使用[key]添加或修改元素

如果创建字典的时候同一个键出现了两次，那么后面出现的值会取代之前的值。

```
a = {'a':'b', 'a':'c', 'a':'d'}
print(a)

tos = ('ab', 'ac', 'ad')
print(dict(tos))

{'a': 'd'}
{'a': 'd'}
```

#### 3.4.4 使用update()合并字典

```
a = {'a':'b', 'c':'d', 'e':'f'}
b = {'a':'x', 'd':'e'}
a.update(b)
print(a)
print(b)

{'a': 'x', 'c': 'd', 'e': 'f', 'd': 'e'}
{'a': 'x', 'd': 'e'}
```

#### 3.4.5 使用del删除具有指定键的元素

```
a = {'a':'b', 'c':'d', 'e':'f'}
b = {'a':'x', 'd':'e'}
a.update(b)
print(a)
print(b)
del a['d']
print(a)

{'a': 'x', 'c': 'd', 'e': 'f', 'd': 'e'}
{'a': 'x', 'd': 'e'}
{'a': 'x', 'c': 'd', 'e': 'f'}
```

#### 3.4.6 使用clear()删除所有元素

```
a = {'a':'b', 'c':'d', 'e':'f'}
a.clear()
print(a)
```

#### 3.4.7 使用in判断是否存在

```
a = {'a':'b', 'c':'d', 'e':'f'}
print('a' in a)
print('Y' in a)
print(1 in a)

True
False
False
```

#### 3.4.8 使用[key]获取元素

- 如果key存在，则返回对应的value
- 如果key不存在，则产生异常
    - 使用in进行提前判断
    - 使用get()方法进行获取
        - 使用`a.get(key, default_value)`可以在键不存在的时候返回指定值

```
a = {'a':'b', 'c':'d', 'e':'f'}

print(a['a'])

print(a.get('c'))

print(a.get('x', 'No this value'))

if('x' in a):
    print("a contains 'x'")
else:
    print("a not contains 'x'")

b
d
No this value
a not contains 'x'   
```

#### 3.4.9 使用keys()获取所有键

```
a = {'a':'b', 'c':'d', 'e':'f'}
b = a.keys()
print(b)
print(list(b))

dict_keys(['a', 'c', 'e'])
['a', 'c', 'e']
```

python3中keys()返回dict_keys，python2中返回list。

区别在于dict_keys性能好，返回list则需要时间和空间来创建这个list。

#### 3.4.10 使用values()获取所有值

和keys()很像，不过是返回了dict_values类型。

```
a = {'a':'b', 'c':'d', 'e':'f'}
b = a.values()
print(b)
print(list(b))

dict_values(['b', 'd', 'f'])
['b', 'd', 'f']
```

#### 3.4.11 使用items()获取所有键值对

和keys()很像，不过是返回了dict_items类型。

```
a = {'a':'b', 'c':'d', 'e':'f'}
b = a.items()
print(b)
print(list(b))

dict_items([('a', 'b'), ('c', 'd'), ('e', 'f')])
[('a', 'b'), ('c', 'd'), ('e', 'f')]
```

#### 3.4.12 使用=赋值，使用copy()复制

与列表一样，对字典内容进行的修改会反映到所有与之相关联的变量名上，可以用copy()来避免。

```
a = {'a':'b', 'c':'d', 'e':'f'}
b = a
c = a.copy()
a['a'] = 'x'
print(a)
print(b)
print(c)

{'a': 'x', 'c': 'd', 'e': 'f'}
{'a': 'x', 'c': 'd', 'e': 'f'}
{'a': 'b', 'c': 'd', 'e': 'f'}
```

### 3.5 集合

集合类似于字典的键。

#### 3.5.1 使用set()创建集合

empty_set = set()

even_numbers = {1, 2, 3, 4, 5}

之所以不能使用`{}`来创建集合，是因为这个符号创建的是字典。

#### 3.5.2 使用set()将其他类型转换为集合

创建后，重复的值只会出现一次。如果是从字典类型转换，则只有键会被使用。

可以从列表、字符串、元组、字典来创建。

#### 3.5.3 使用in测试值是否存在

```
a = {1, 2, 3, 4, 5}
print(1 in a)
print('1' in a)

True
False
```

#### 3.5.4 合并及运算符

- 交集：set1 & set2，仅保留两者相同的。小技巧：任何集合 & 空集 等于空集。也可以用a.intersection(b)来替代。
- 并集：set1 | set2，将两者合并，相同的会自动去重复。也可以用a.union(b)来替代。
- 差集：set1 - set2，保留set1中有，但是set2中没有的部分，删掉set2中重复的部分。也可以用a.difference(b)来替代。
- 异或集：set1 ^ set2，仅在集合中出现一次的，去掉两者都有的。也可以用a.symmetric_difference(b)来替代。
- 子集：set1 <= set2，则set1是set2的子集。也可以用a.issubset(b)来替代。
- 真子集：set1 < set2，则set1是set2的真子集。
- 超集：set1 >= set2，则set1是set2的超集，和子集概念相反。也可以用a.issuperset(b)来替代。
- 真超集：set1 > set2，则set1是set2的真超集。

### 3.6 比较几种数据结构

```
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho':'banjo', 'Chico':'piano', 'Harpo':'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}
print(marx_list)
print(marx_tuple)
print(marx_dict)
print(marx_set)

['Groucho', 'Chico', 'Harpo']
('Groucho', 'Chico', 'Harpo')
{'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
{'Chico', 'Harpo', 'Groucho'}
```

其中，list、tuple和dict都可以用[]进行访问。

当元组仅包含1个元素的时候，需要以逗号结尾。

### 3.7 建立大型数据结构

可以使用各种内置的数据结构自由组合成更大、更复杂的结构。

### 3.8 练习

无

第4章 Python外壳：代码结构
--------------------------------------------

### 4.1 使用#注释

\#号只能做单行注释，Python中没有多行注释的符号。

### 4.2 使用\连接

- 多行连成一行，需要在行尾加上\
- 表达式占用多行的时候，也需要行连接符\，比如：

```
a = 1 + 2 \
    + 3
print(a)

6
```

### 4.3 使用if、elif和else进行比较

- 使用if、elif和else可以进行条件判断
- 表达式通过换行和缩进来区别语句块
- 条件指令行末尾需要用冒号（:）否则会出错

判断语句对布尔值进行判断，如果是个表达式，则会计算后再进行判断。

下面的语句是一样的：

- 5 < x and x < 10
- (5 < x) and (x < 10)
- 5 < x < 10

下面的值也被认为是False，除此以外都被认定为True：

- 布尔：False
- null类型：None
- 整形：0
- 浮点型：0.0
- 空字符串：''
- 空列表：[]
- 空元组：()
- 空字典：{}
- 空集合：set()

### 4.4 使用while进行循环

#### 4.4.1 使用break跳出循环

和C语言一样。

#### 4.4.2 使用continue跳到循环开始

和C语言一样。

#### 4.4.3 循环外使用else

如果while语句是正常执行结束，而不是遇到break结束，则执行这个else。

如果遇到了break结束，则不会执行这个else。

```
x = 3
y = 6
i = 0
while i < x:
    if i == y: #never
        print("i == " + str(y))
        break
    else:
        print("i == " + str(i))
    i += 1
else:
    print("not match y, no encounter break")


i == 0
i == 1
i == 2
not match y, no encounter break
```

### 4.5 使用for迭代

```
x = {"a":1, "b":2, "c":3}
for key, value in x.items():
    print("key:" + key + ", value:" + str(value))

key:a, value:1
key:b, value:2
key:c, value:3
```

#### 4.5.1 使用break跳出循环

和while一致。

#### 4.5.2 使用continue跳到循环开始

和while一致。

#### 4.5.3 循环外使用else

和while一致。

#### 4.5.4 使用zip()并行迭代

使用zip()函数可以遍历多个序列，在具有相同位移的项之间创建元组。

zip()函数在最短序列“用完”时就会停止。

```
a = ['i', 'j', 'k']
b = ['1', '2', '3', '4']

c1 = zip(a, b)
c2 = zip(a, b)

d = list(c1)
e = list(c1)
f = dict(c2)

print(type(c1))
print(type(c2))
print(c1)
print(c2)
print(d)
print(e)
print(f)

<class 'zip'>
<class 'zip'>
<zip object at 0x10e4cf048>
<zip object at 0x10e4cfcc8>
[('i', '1'), ('j', '2'), ('k', '3')]
[]
{'i': '1', 'j': '2', 'k': '3'}
```

注意到这个例子中，c1被两次转换成了list，第二次得到的结果是空。

#### 4.5.5 使用range()生成自然数序列

range()函数返回在特定区间的自然数序列，不需要创建和存储复杂的数据结构，例如列表或元组。这允许在不使用计算机全部内存的情况下创建较大的区间，也不会使你的程序崩溃。

`range(start, stop, step)`：

- start默认为0。
- stop产生的最后一个数的值是stop的前一个，唯一必填的值。
- step的默认值是1，反向创建自然数序列，可以使用-1。

```
for i in range(3, 23, 5):
    print(str(i))
    
print('-----')
for i in range(23-5, 3-1, -5):
    print(str(i))

3
8
13
18
-----
18
13
8
3
```

#### 4.5.6 其他迭代方式

第8章将介绍文件之间的迭代。
在第6章中，你会看到如何在自己创建的对象之间迭代。

### 4.6 推导式

#### 4.6.1 列表推导式

```
[ expression for item in iterable ]

[ expression for item in iterable if condition]

[ expression for item1 in iterable if condition for item2 in iterable if condition]
```

expression：列表生成值，可以是表达式。把循环的结果放在结果列表中。

```
rows = range(1,4)
cols = range(1,3)
cells1 = [(row, col) for row in rows for col in cols]
for cell in cells1:
    print(cell)
    
print('-------')

rows = range(1,12)
cols = range(1,8)
cells2 = [(row, col) for row in rows if row % 2 == 0 for col in cols if col % 3 == 0]
for cell in cells2:
    print(cell)

(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
-------
(2, 3)
(2, 6)
(4, 3)
(4, 6)
(6, 3)
(6, 6)
(8, 3)
(8, 6)
(10, 3)
(10, 6)
```

#### 4.6.2 字典推导式

```
{ key_expression : value_expression for expression in iterable }
```

下面的例子统计每个字母在字符串中出现的次数：

```
str1 = '{ key_expression : value_expression for expression in iterable }'

x = { letter : str1.count(letter) for letter in str1 }
print(x)

# 优化，避免遍历相同的字符太多次
x = { letter : str1.count(letter) for letter in set(str1) }
print(x)

{'{': 1, ' ': 8, 'k': 1, 'e': 10, 'y': 1, '_': 2, 'x': 3, 'p': 3, 'r': 5, 's': 6, 'i': 5, 'o': 4, 'n': 4, ':': 1, 'v': 1, 'a': 2, 'l': 2, 'u': 1, 'f': 1, 't': 1, 'b': 1, '}': 1}
{'o': 4, 'n': 4, 'i': 5, 'r': 5, 'v': 1, ' ': 8, 'u': 1, 's': 6, '}': 1, '_': 2, 'p': 3, 'y': 1, 'l': 2, 'k': 1, ':': 1, 't': 1, '{': 1, 'x': 3, 'a': 2, 'f': 1, 'b': 1, 'e': 10}
```

#### 4.6.3 集合推导式

```
{ expression for expression in interable}
```

和字典类似：

```
x = { number for number in range(1,6) if number % 3 == 1}
print(x)

{1, 4}
```

#### 4.6.4 生成器推导式

```
number_thing = (number for number in range(1,6))
print(type(number_thing))

<class 'generator'>
```

一个生成器只能运行一次。列表、集合、字符串和字典都存储在内存中，但是生成器仅在运行中产生值，不会被存下来，所以不能重新使用或者备份一个生成器。

```
number_thing = (number for number in range(1,6))
number_list = list(number_thing)
try_again = list(number_thing)
print(number_list)
print(try_again)

[1, 2, 3, 4, 5]
[]
```

### 4.7 函数

如果函数不显式调用return函数，那么会默认返回None。

#### 4.7.1 位置参数

意思是按照函数声明的参数的位置，调用时候依次传递参数。

#### 4.7.2 关键字参数

```
def func(p1, p2, p3):
    return {'p1':p1, 'p2':p2, 'p3':p3}

print(func(p2='Hello', p1='Hi', p3='Hey'))

{'p1': 'Hi', 'p2': 'Hello', 'p3': 'Hey'}
```
如果同时使用位置参数和关键字参数两种方式调用函数，位置参数必须放置于关键字参数之前。如果参数被传递多次，则会报错。

```
def func(p1, p2, p3):
    return {'p1':p1, 'p2':p2, 'p3':p3}

print(func('Hello', p3='Hi', p2='Hey'))

{'p1': 'Hello', 'p2': 'Hey', 'p3': 'Hi'}
```

#### 4.7.3 指定默认参数值

默认参数值在函数定义时已经计算出来，而不是在程序运行时。

```
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
    
buggy('a')
buggy('b')
buggy('c')
buggy('d')

['a']
['a', 'b']
['a', 'b', 'c']
['a', 'b', 'c', 'd']
```

```
def buggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
    
buggy('a')
buggy('b')
buggy('c')
buggy('d')

['a']
['b']
['c']
['d']
```

#### 4.7.4 使用*收集位置参数

当参数被用在函数内部时，星号将一组可变数量的位置参数集合成参数值的元组。

```
def print_args(yourname, *args, last):
    print('Hi, ' + yourname)
    print('Positional argument tuple:', args)
    print(type(args))
    print(last)
    
print_args('volnet',1,2,3,4,'Thanks', last='Bye!')

Hi, volnet
Positional argument tuple: (1, 2, 3, 4, 'Thanks')
<class 'tuple'>
Bye!
```

#### 4.7.5 使用**收集关键字参数

使用两个星号可以将参数收集到一个字典中，参数的名字是字典的键，对应参数的值是字典的值。

```
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
print_kwargs(Name='volnet', Age=50)

Keyword arguments: {'Name': 'volnet', 'Age': 50}
```

```
def print_args_kwargs(*args, **kwargs):
    print(args)
    print('----')
    print(kwargs)
    
print_args_kwargs('0',1,2,3,4,'Thanks', last='Bye!')

('0', 1, 2, 3, 4, 'Thanks')
----
{'last': 'Bye!'}
```
如果把`*args`和`**kwargs`的位置参数混合起来，它们必须按照顺序出现。

#### 4.7.6 文档字符串

在函数内第一行可以写单行或多行注释。

可以用`help()`和`print(funcname.__doc__)`查看注释。

```
def echo1(a):
    'echo1 returns its input argument'
    return a

def echo2(*args):
    '''
    echo2 returns its input arguments
    multiline
    '''
    return b

help(echo1)
print('-------')
help(echo2)
print('-------')
print(echo1.__doc__)
print('-------')
print(echo2.__doc__)


Help on function echo1 in module __main__:

echo1(a)
    echo1 returns its input argument

-------
Help on function echo2 in module __main__:

echo2(*args)
    echo2 returns its input arguments
    multiline

-------
echo1 returns its input argument
-------

    echo2 returns its input arguments
    multiline
    
```

#### 4.7.7 一等公民：函数

函数和数字、字符串、元组、列表、字典等一样，都是python的一等公民。

函数也可以作为参数进行传递，传递函数的名字（不包含括号）。函数后面的括号表示调用函数。

#### 4.7.8 内部函数

可以在函数的内部再定义一个函数。

```
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))

"We are the knights who say: 'Ni!'"
```

#### 4.7.9 闭包

内部函数可以看作一个闭包。闭包是一个可以由另一个函数动态生成的函数，并且可以改变和存储函数外创建的变量的值。

```
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(a())
print(b())

We are the knights who say: 'Duck'
We are the knights who say: 'Hasenpfeffer'
```

#### 4.7.10 lambda()函数

```
lambda param : expression
```

```
def hello(func, arg1, arg2):
    func(arg1, arg2)
    
def my_func(items1, items2=None):
    for arg in list(items1):
        print('1.' + arg.capitalize())
    if arg is not None:
        for arg in list(items2):
            print('2.' + arg)
        
hello(my_func, 'how', 'are')
print('-----')
hello(lambda item1,item2: print(item1 + ' ' + item2), 'what', 'is')

1.H
1.O
1.W
2.a
2.r
2.e
-----
what is
```

### 4.8 生成器

返回值使用`yield`语句声明而不是`return`。

```
def my_range(first=0, last=10000, step=1):
    number = first
    while number < last:
        yield number
        number += step
        
for i in my_range(0,5):
    print(i)

0
1
2
3
4
```

### 4.9 装饰器

一个函数可以有多个装饰器。

靠近函数定义（def上面）的装饰器最先执行。

```
def document_it(func):
    print('-- document_it run')
    def new_function1(*args, **kwargs):
        print('---- new_function1 run')
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function1

def add_ints(a, b):
    return a + b

x = add_ints(3, 5)
print(x)

cooler_add_ints = document_it(add_ints)
y = cooler_add_ints(3, 5)
print('i =', y)

print('-------')

def square_it(func):
    print('-- square_it run')
    def new_function2(*args, **kwargs):
        print('---- new_function2 run')
        result = func(*args, **kwargs)
        return result * result
    return new_function2

@document_it
@square_it
def add_ints1(a, b):
    return a + b

print('j =', add_ints1(3, 5))

print('-------')

@square_it
@document_it
def add_ints2(a, b):
    return a + b
print('k =', add_ints2(3, 5))

8
-- document_it run
---- new_function1 run
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
i = 8
-------
-- square_it run
-- document_it run
---- new_function1 run
Running function: new_function2
Positional arguments: (3, 5)
Keyword arguments: {}
---- new_function2 run
Result: 64
j = 64
-------
-- document_it run
-- square_it run
---- new_function2 run
---- new_function1 run
Running function: add_ints2
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
k = 64
```

### 4.10 命名空间和作用域

- 在局部作用域中不能修改全局作用域的内容
- 如果需要使用到全局作用域，则需要使用`globals xxx`关键字
- 使用`locals()`, `globals()`函数可以显示局部和全局变量
- 使用`_`和`__`的开头和结束的名称都是Python的保留用法。

```
animal = 'bird'
def local_func1():
    animal = 'monkey'
    print(animal)

def local_func2():
    global animal
    print('animal=', animal) # 一旦使用，就被认为局部作用域内的animal是全局变量了。
    animal = 'monkey'
    print(animal)
    
def local_func3():
    print('animal=', animal) # 一旦使用，就被认为局部作用域内的animal是全局变量了。
    animal = 'monkey'
    print(animal)
    
    
local_func1()
print('-------')
local_func2()
print('-------')
local_func3()

monkey
-------
animal= bird
monkey
-------
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-84-50e43398b0a1> in <module>()
     20 local_func2()
     21 print('-------')
---> 22 local_func3()

<ipython-input-84-50e43398b0a1> in local_func3()
     11 
     12 def local_func3():
---> 13     print('animal=', animal) # 一旦使用，就被认为局部作用域内的animal是全局变量了。
     14     animal = 'monkey'
     15     print(animal)

UnboundLocalError: local variable 'animal' referenced before assignment

```

```
animal = 'bird'
def local_func4():
    animal = 'monkey'
    print(animal)
    print('locals:', locals())
    
print('globals:', globals())
local_func4()

globals: {'__name__': '__main__', '__doc__': 'Automatically created module for IPython interactive environment', '__package__': None, '__loader__': None, '__spec__': None, '__builtin__': <module 'builtins' (built-in)>, '__builtins__': <module 'builtins' (built-in)>, '_ih': ['', "animal = 'bird'\ndef local_func4():\n    animal = 'monkey'\n    print(animal)\n    print('locals:', locals())\n    \nprint('globals:', globals())\nlocal_func4()"], '_oh': {}, '_dh': ['/Users/gongcen/VolnetGitHub/volnet.github.io/docs/book/IntroducingPython/samples/chapter03'], 'In': ['', "animal = 'bird'\ndef local_func4():\n    animal = 'monkey'\n    print(animal)\n    print('locals:', locals())\n    \nprint('globals:', globals())\nlocal_func4()"], 'Out': {}, 'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x1096fb6a0>>, 'exit': <IPython.core.autocall.ZMQExitAutocall object at 0x1097456d8>, 'quit': <IPython.core.autocall.ZMQExitAutocall object at 0x1097456d8>, '_': '', '__': '', '___': '', '_i': '', '_ii': '', '_iii': '', '_i1': "animal = 'bird'\ndef local_func4():\n    animal = 'monkey'\n    print(animal)\n    print('locals:', locals())\n    \nprint('globals:', globals())\nlocal_func4()", 'animal': 'bird', 'local_func4': <function local_func4 at 0x10981e488>}
monkey
locals: {'animal': 'monkey'}
```

### 4.11 使用try和except处理错误

```
try:
    expression
except exceptiontype as name:
    expression
except exceptiontype as name:
    expression
except:
    expression_default
```

### 4.12 编写自己的异常

```
# 定义异常
class CustomException(Exception):
    pass

# 抛出异常
raise CustomException(params)
```
```
class MyException1(Exception):
    pass
class MyException2(Exception):
    print('MyException2 definition')
    
def my_func1(item):
    raise MyException1(item)
def my_func2(item):
    raise MyException2(item)
def my_func3(item):
    raise item / 0
    
def run(func, arg):
    try:
        func(arg)
    except MyException1 as exp1:
        print('MyException1 catched.')
    except MyException2 as exp2:
        print('MyException2 catched.')
    except:
        print('OtherException catched.')
        
print('1.')
run(my_func1, 'a1')
print('-------')
print('2.')
run(my_func2, 'a2')
print('-------')
print('3.')
run(my_func3, 'a3')

MyException2 definition
1.
MyException1 catched.
-------
2.
MyException2 catched.
-------
3.
OtherException catched.
```

第5章 Python盒子：模块、包和程序
--------------------------------------------

### 5.1 独立的程序

将代码保存成文件（通常以`.py`为后缀），然后用`python xxx.py`来运行。

### 5.2 命令行参数

使用`sys.argv`可以读取命令行参数。

@commandline.py

```
import sys
print('Program arguments:', sys.argv)
```

`python commandline.py hello tra lala`

```
Program arguments: ['commandline.py', 'hello', 'tra', 'lala']
```

### 5.3 模块和import语句

#### 5.3.1 导入模块

模块是一个python文件，例如：filename.py。模块名称是文件名（不含.py）。

用语句`import filename`可以在另一个文件中导入模块。

用语句`from filename import functionname`可以导入单个函数。

用语句`filename.functionname`或者`functionname`均可调用函数，后者不应该与程序中的其他对象同名。

可以在文件的开头写这些，也可以在函数里写这些。

#### 5.3.2 使用别名导入模块

用语句`import filename as xx`或者`from filename import functionname as fn`可以给模块或函数定义别名。

#### 5.3.3 导入模块的一部分

用`from filename import functionname as fn`定义函数的别名后，在调用的时候，不仅可以直接写`functionname`也可以使用别名`fn`。

#### 5.3.4 模块搜索路径

用这个语句可以查看模块搜索的路径，路径优先级从上往下，找到后就不往后找了。

```
import sys
for place in sys.path:
    print(place)


/Users/username/anaconda3/lib/python36.zip
/Users/username/anaconda3/lib/python3.6
/Users/username/anaconda3/lib/python3.6/lib-dynload
/Users/username/anaconda3/lib/python3.6/site-packages
/Users/username/anaconda3/lib/python3.6/site-packages/aeosa
/Users/username/anaconda3/lib/python3.6/site-packages/IPython/extensions
/Users/username/.ipython
```

需要特别注意的是，返回值中的第一行是空行，代表当前路径。

### 5.4 包

可以把多个模块组织成文件层次，称之为包。

书中例子是这样组织目录的：

```
boxes/weather.py
boxes/sources/daily.py
boxes/sources/weekly.py
boxes/sources/__init__.py
```

于是整个`boxes`就是一个包。

weather.py文件中可以这么调用：

```
from sources import daily, weekly
……
```

### 5.5 Python标准库

- Python官方文档：http://docs.python.org/3/library
- 官方使用指南：https://docs.python.org/3.3/tutorial/stdlib.html
- Doug Hellmann的网站Python Module of the Week：http://pymotw.com/2/contents.html
- Doug Hellmann的书《[The Python Standard Library by Example](https://www.amazon.cn/dp/0134291050/ref=sr_1_1?ie=UTF8&qid=1524667895&sr=8-1&keywords=The+Python+Standard+Library+by+Example)》

#### 5.5.1 使用setdefault()和defaultdict()处理缺失的键

setdefault的含义：仅在原有Key不存在的时候，会在字典中添加一项。

```
periodic_table = {'Hydrogen':1, 'Helium':2}

print(periodic_table['Hydrogen'])
print(periodic_table.get('Hydrogen'))

periodic_table['Hello'] = 3

# setdefault的含义：仅在原有Key不存在的时候，会在字典中添加一项

# 如果Key不存在，则设定对应的值
periodic_table.setdefault('World', 4)
# 如果Key已经存在，则维持原来的值不变
periodic_table.setdefault('Hello', 999)

print(periodic_table)

1
1
{'Hydrogen': 1, 'Helium': 2, 'Hello': 3, 'World': 4}
```

defaultdict的含义是设定字典的默认值。

```
from collections import defaultdict

table0 = defaultdict(int)
table1 = defaultdict(lambda: 'default value')

def myDefaultValue():
    return 100;

table2 = defaultdict(myDefaultValue)

print(table0)
print(table1)
print(table2)
print('-----------')
print(table0['Hello'])
print(table1['Hello'])
print(table2['Hello'])

defaultdict(<class 'int'>, {})
defaultdict(<function <lambda> at 0x104eb8598>, {})
defaultdict(<function myDefaultValue at 0x104eb89d8>, {})
-----------
0
default value
100
```

#### 5.5.2 使用Counter()计数

https://docs.python.org/3.3/library/collections.html?highlight=counter#collections.Counter

Counter函数类似SQL中的聚合函数，可以对可迭代的对象进行计数，Counter对象还可以进行`+`、`-`、`&`、`|`的操作。

`.most_common([n])`按降序返回Count数值比n大的元素，如果不设置n，则按降序返回所有值。

```
from collections import Counter
counter1 = Counter(['Hello', 'Hello', 'World', 'World', 'World', 'ViVi'])
counter2 = Counter(['Hello', 'World', 'Volnet', 'MacBook Pro', 'MacBook Pro'])
print(counter1)
print(counter2)
print(counter1['Hello'])
print(counter1['WithoutKey'])
print(counter1)
print('--------')
counter1SortedDescAll = counter1.most_common()
counter1SortedDescMoreThan2 = counter1.most_common(2)
print(counter1SortedDescAll)
print(counter1SortedDescMoreThan2)
print('--------')
counterAdd = counter1 + counter2
counterSubstract = counter1 - counter2
counterAnd = counter1 & counter2
counterOr = counter1 | counter2
print(counterAdd)
print(counterSubstract)
print(counterAnd)
print(counterOr)

Counter({'World': 3, 'Hello': 2, 'ViVi': 1})
Counter({'MacBook Pro': 2, 'Hello': 1, 'World': 1, 'Volnet': 1})
2
0
Counter({'World': 3, 'Hello': 2, 'ViVi': 1})
--------
[('World', 3), ('Hello', 2), ('ViVi', 1)]
[('World', 3), ('Hello', 2)]
--------
Counter({'World': 4, 'Hello': 3, 'MacBook Pro': 2, 'ViVi': 1, 'Volnet': 1})
Counter({'World': 2, 'Hello': 1, 'ViVi': 1})
Counter({'Hello': 1, 'World': 1})
Counter({'World': 3, 'Hello': 2, 'MacBook Pro': 2, 'ViVi': 1, 'Volnet': 1})
```

#### 5.5.3 使用有序字典OrderedDict()按键排序

一般的字典，添加键是按顺序的，但是实际上运行迭代器的时候，不一定按照添加的顺序来返回。

使用OrderedDict，则会记住添加键的顺序，然后运行迭代器的时候，按照添加顺序来返回。

```
from collections import OrderedDict
orderDict = OrderedDict([('Hello', 'Ok'), ('World', 'Yes'), ('Asia', 'No')])
orderDict['Nick'] = 'Bye'
print(orderDict)
for item in orderDict:
    print(item)
```

#### 5.5.4 双端队列：栈+队列

- `popleft()`：从左侧移出
- `pop()`：从右侧移出
- `word[::-1]`可以实现类似`reverse()`的效果。

```
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while(len(dq) > 1):
        a = dq.popleft()
        b = dq.pop()
        print('left:' + a + ' right:' + b)
        if a != b:
            return False
    return True

print(palindrome('abccba'))
print('----------------')
print(palindrome('abcba'))
print('----------------')
print(palindrome('a'))
print('----------------')
print(palindrome('ab'))
print('################')

def palindrome2(word):
    return word == word[::-1]

print(palindrome2('abccba'))
print('----------------')
print(palindrome2('abcba'))
print('----------------')
print(palindrome2('a'))
print('----------------')
print(palindrome2('ab'))

left:a right:a
left:b right:b
left:c right:c
True
----------------
left:a right:a
left:b right:b
True
----------------
True
----------------
left:a right:b
False
################
True
----------------
True
----------------
True
----------------
False
```

#### 5.5.5 使用itertools迭代代码结构

itertools包含一些迭代器函数。

- `chain`：将多个元素组合到一个迭代器中
- `cycle`：循环输出迭代结果
- `accumulate`：在迭代的时候，累积执行前面的值，第二个参数可以指定一个累积函数，未指定累积函数的，默认使用累加。

```
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
    
print('----------------')

stop = 0
for item in itertools.cycle([1, 2]):
    stop += 1
    print(item)
    if stop == 3:
        break
print('----------------')

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
print('----------------')    

def mutiply(a, b):
    return a * b
for item in itertools.accumulate([1, 2, 3, 4], mutiply):
    print(item)

1
2
a
b
----------------
1
2
1
----------------
1
3
6
10
----------------
1
2
6
24
```

#### 5.5.6 使用pprint()友好输出

增加输出结果的可读性。

```
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
print('-------------')

pprint.pprint(stuff)
print('-------------')

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)
print('-------------')
tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)


[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']
-------------
[['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']
-------------
[['spam', 'eggs', 'lumberjack',
  'knights', 'ni'],
 'spam', 'eggs', 'lumberjack', 'knights',
 'ni']
-------------
('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))
```

### 5.6 获取更多Python代码

可以从PyPi（ http://pypi.python.org ）、github（ http://github.com/Python ）、readthedocs（ https://readthedocs.org/ ）获得代码。

### 5.7 练习

无

第6章 对象和类
--------------------------------------------

第7章 像高手一样玩转数据
--------------------------------------------

第8章 数据的归宿
--------------------------------------------

第9章 剖析Web
--------------------------------------------

第10章 系统
--------------------------------------------

第11章 并发和网络
--------------------------------------------

第12章 成为真正的Python开发者
--------------------------------------------

附录A Python的艺术
--------------------------------------------

附录B 工作中的Python
--------------------------------------------

附录C Python的科学
--------------------------------------------

附录D 安装Python 3
--------------------------------------------

附录E 习题解答
--------------------------------------------

附录F 速查表
--------------------------------------------

作者介绍
--------------------------------------------

封面介绍
--------------------------------------------