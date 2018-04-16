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

第5章 Python盒子：模块、包和程序
--------------------------------------------

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