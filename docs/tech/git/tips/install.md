Install Git On CentOS
==========================

CentOS Minimal的yum install git只能安装1.8版本的git。 为了能用上最新的git版本（目前是2.18.*），只能从Source Code开始。

1. 下载源码包：从这里选一个`https://mirrors.edge.kernel.org/pub/software/scm/git/` 或者直接`curl -o git-2.18.0.tar.gz https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.18.0.tar.gz`

2. 解压压缩包`tar -zxf git-2.18.0.tar.gz && cd git-2.18.0`

3. 从yum安装各种包：`yum install autoconf curl-devel expat-devel gettext-devel openssl-devel perl-devel zlib-devel asciidoc xmlto`

4. 安装docbook2X，这个在yum源中没有，需要自己下载包安装。

```
$ curl -o docbook2X-0.8.8-17.el7.x86_64.rpm http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/d/docbook2X-0.8.8-17.el7.x86_64.rpm
$ rpm -Uvh docbook2X-0.8.8-17.el7.x86_64.rpm
```

5. 编译并安装git，命令参考 https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 页面最后

```
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info
```

6. 重启服务器：（ 否则可能会遇到Unable to find remote helper for 'https' ）

```
$ reboot now
```

7. 测试：

```
$ git clone https://github.com/volnet/v-labs.git
$ cd v-labs
$ touch test.txt
$ git add .
$ git commit -m "test git install"
$ git push -u
```

See also
--------------------------

1. [English Version](https://stackoverflow.com/a/51102026/310226)