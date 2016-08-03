Git凭证存储
============

今天给自己提了一个问题，当我们在github.com或者gitlab.com上面新建仓库，并克隆到本地的时候。首次使用，我们会被问及密码，但是这个密码存在哪里呢？

带着这个问题，我开始搜索，并在[《Pro Git》7.14 Git-工具-凭证存储](https://git-scm.com/book/zh/v2/Git-工具-凭证存储)中读到了完整的解答，但是当我第一次阅读的时候，并没有太清楚它所要表达的意思，于是我不断尝试后，总算是有所明白。

本文就作为一个解读贴，稍作补充。

凭证存储究竟要解决什么问题？
------------------------

众所周知，我们通常用SSH和HTTP协议来访问远程仓库。SSH协议并不适用于这里讨论的凭证存储。这里重点要描述的其实是HTTP协议下的凭证存储问题。

为什么会有这个问题呢？因为git使用HTTP协议访问远程仓库进行操作的时候，每个请求，都需要带着用户名和密码以及一个随机码防止重放攻击。

所以《Pro Git》中的第一部分，就指出，默认情况下每次进行操作的时候，都需要提供用户名和密码。

默认情况下你为什么没有被要求每次都输入用户名密码？
------------------------------------------

《Pro Git》中的第一部分，针对这个问题也给出了解释。

如果你是Mac系统，git默认是提供`osxkeychain`辅助程序来管理你的密码，以至于每次你当你需要提供用户名和密码的时候，`osxkeychain`辅助程序都默默帮你填写了。

如果你是Windows系统，你可能已经安装了`git-credential-winstore`了。

除此之外，你也可以使用`git-credential-store`和`git-credential-cache`来管理密码，前者明文存储密码，后者存在内存中。

而这几种方式都可以同时存在！

我们该如何选择/设置辅助程序的类型？
------------------------------

在回答这个问题前，我们先简单看一下，什么是辅助程序？这个翻译对应的其实是credential.helper配置项，我们可以通过如下命令查看当前配置：

```
git config --list | grep credential
```

从Mac看，默认会输出：

```
include.path=.gitcredential

credential.helper=osxkeychain
```

对应的也就是Mac的“钥匙串”系统，我们可以通过Mac系统菜单页面“其他->钥匙串访问”功能，搜索git关键字查看。

接下来，我们再设置一个明文存储的，也就是store类型的全局存储，使用下面的命令来试一下：

```
git config --global credential.helper store
```

虽然原文中提到store中提到可以使用--file命令，但是实测--global命令下无效。

但是可以通过直接编辑配置文件的方式来达到目的：

设置全局的：

```
git config --global -e
```

设置针对当前项目的：

```
git config --local -e
```

然后在[credential]配置节下添加：

```
        helper = store --file $HOME/git-credentials/global.gitcredentials
        helper = store
```

两行中，第一行代表指定目录，第二行代表使用[默认路径](https://git-scm.com/docs/git-credential-store)。

（这里我们分别对--global和--local都做了设置）

![](git-credentials/001.png)

再次运行后

```
git config --list | grep credential
```

从Mac看，会输出：

```
include.path=.gitcredential

credential.helper=osxkeychain

credential.helper=store --file $HOME/git-credentials/global.gitcredentials

credential.helper=store

credential.helper=store --file $HOME/git-credentials/v-labs.gitcredentials
```

也就是说，不仅支持osxkeychain模式，还同时支持了store模式。

为了测试效果，打开“钥匙串访问”程序（如果是Mac的话），搜索git，把所有出现的都删掉。

这时候使用`git push`命令向远程提交变更。（因为刚刚设置了较多的辅助程序，因此会比较慢）。

这时如果提示输入用户名密码，就按正确的值输入。当你被提示成功后，这期间，我们刚刚输入的密码，都被存到了我们设置的所有凭证存储中。

在“钥匙串访问”程序中，我们也会看到一条新增的凭证信息。

我们既然存储了密码，那密码在哪，又是什么呢？
-------------------------------------

先来看几个使用store的选项，我们刚刚既在指定路径也在默认路径上进行了设置，那么我们就分别输入下面三个命令，就可以查看到密码了：

```
localhost:~ gongcen$ cd git-credentials/

localhost:git-credentials gongcen$ ls
global.gitcredentials	v-labs.gitcredentials

localhost:git-credentials gongcen$ cat global.gitcredentials 
https://volnet:123321@github.com

localhost:git-credentials gongcen$ cat v-labs.gitcredentials 
https://volnet:123321@github.com

localhost:git-credentials gongcen$ cat ~/.git-credentials 
https://volnet:123321@github.com
```

当然，也可以用[《Pro Git》](https://git-scm.com/book/zh/v2/Git-工具-凭证存储)中提到的`git credential-store --file ~/git.store store`命令来读取了。

那么，使用Mac的osxkeychain的密码，是否可以拿回来呢？

答案是肯定的！

```
localhost:git-credentials gongcen$ git credential-osxkeychain get
protocol=https
host=github.com

password=123321
username=volnet
```

由这一点可以看出，在[《Pro Git》](https://git-scm.com/book/zh/v2/Git-工具-凭证存储)中提到的`foo`就是这个辅助程序的名字。

get/store/erase是什么作用？
-----------------------

从[《Pro Git》](https://git-scm.com/book/zh/v2/Git-工具-凭证存储)看，这三个均称为Action，其实也就是从辅助程序获取密码（get）/设置密码（store）/删除密码（erase）。

刚刚的动作中能get到密码了，那么我们尝试删除一下。执行以下命令试一下：

```
localhost:v-labs gongcen$ git credential-osxkeychain erase
protocol=https
host=github.com

```

再次用以下代码验证，将没有返回值。使用“钥匙串访问”程序，也将看不到新添加的凭证。

```
localhost:git-credentials gongcen$ git credential-osxkeychain get
protocol=https
host=github.com

```

那git credential fill是什么用的？
------------------------------

在每次进行访问git push（或其他需要用户名密码的命令）的时候，都会调用该方法，它按照由近及远的思路，尝试向辅助程序获取用户密码，如果成功，就用这个获得的用户密码去访问远程仓库。如果获取不到，就会让用户输入一次，并尝试保存下来。

因此我们第一次使用的时候，会被提示输入用户名密码，就是因为git的内部调用了这个命令。

辅助程序是否可以自己定义呢？
-----------------------

答案当然是肯定的，在[《Pro Git》](https://git-scm.com/book/zh/v2/Git-工具-凭证存储)中也提供了ruby的示例。

刚刚设置了那么多，我想删掉那些store存储怎么处理？
-----------------------------------------

我们可以使用刚刚直接编辑config文件的思路，直接修改后保存。

同时我们需要注意，那些已经被明文保存的密码，我们需要自行删掉。

也可以使用以下命令：

```
git config --global --unset credential.helper -f
git config --local --unset credential.helper -f
rm -rf $HOME/git-credentials
rm ~/.git-credentials 
```

使用下面命令验证，应该已经看不到结果了：

```
localhost:~ gongcen$ git credential-store get
protocol=https
host=github.com

```

至此，所有关于配置相关的内容都已经解释完毕。

结论就是，如果不打算明文存储密码，就尽量使用SSH的方式。

参考资料
-------

1. [《Pro Git》7.14 Git-工具-凭证存储](https://git-scm.com/book/zh/v2/Git-工具-凭证存储)

2. [Git Docs / git-credential-store](https://git-scm.com/docs/git-credential-store)

3. [Git Docs / git-credential-cache](https://git-scm.com/docs/git-credential-cache)

4. [Apple Docs / osxkeychain](https://support.apple.com/en-us/HT201609)

5. [Blog / Git之https或http方式设置记住用户名和密码的方法](http://transcoder.baidu.com/from=844b/bd_page_type=1/ssid=0/uid=0/pu=usm%400%2Csz%401320_2001%2Cta%40iphone_1_9.3_3_601/baiduid=284644EE1E1522FA471ED7609292BD84/w=0_10_git+http+方式+密码+存储/t=iphone/l=3/tc?ref=www_iphone&lid=12231686873911203779&order=1&fm=alop&tj=www_normal_1_0_10_title&vit=osres&m=8&srd=1&cltj=cloud_title&asres=1&title=git之https或http方式设置记住用户名和密码的..._博客园&dict=30&sec=14196&di=fe20c4c3da1e55f4&bdenc=1&tch=124.0.0.0.0.0&nsrc=IlPT2AEptyoA_yixCFOxXnANedT62v3IEQGG_ytK1DK6mlrte4viZQRAVTbgKCbIUICb9n00sqcCuXOg27En6so4g43&eqid=a9bfae67d34918001000000157a1e80c&wd=&clk_info=%7B%22srcid%22%3A%22www_normal%22%2C%22tplname%22%3A%22www_normal%22%2C%22t%22%3A1470228496815%2C%22xpath%22%3A%22div-a-h3%22%7D)

6. [Blog / 使用git-credential-winstore保存https访问密码](http://transcoder.baidu.com/from=1099b/bd_page_type=1/ssid=0/uid=0/pu=usm%400%2Csz%401320_2001%2Cta%40iphone_1_9.3_3_601/baiduid=A01E3FB73824A156C1F3F154FB7EBC7C/w=0_10_git+http+密码+存储+在哪/t=iphone/l=3/tc?ref=www_iphone&lid=11572465786643165579&order=8&fm=alop&tj=www_normal_8_0_10_title&vit=osres&m=8&srd=1&cltj=cloud_title&asres=1&title=使用git-credential-winstore保存https访问密码%7CNo...&dict=32&sec=14196&di=e46bebb03d84a2ce&bdenc=1&tch=124.65.253.1210.1.99&nsrc=IlPT2AEptyoA_yixCFOxXnANedT62v3IEQGG_yBL1zSnoU_lfbrgHtkfEFWhACbCZpPPdDf0sqdCaC77Njdsjg5Qh3htgCdqjyi8s_Wdrwj2V1pOutwm0hvESStp5fn55P2esRQyKABkKzx7jO4auwYntxaFf22L&eqid=a099a851c43a30001000000157a1e889&wd=&clk_info=%7B%22srcid%22%3A%22www_normal%22%2C%22tplname%22%3A%22www_normal%22%2C%22t%22%3A1470228722116%2C%22xpath%22%3A%22div-a-h3-em2%22%7D)