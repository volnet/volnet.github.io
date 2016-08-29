第一本Docker书
==============

作者：[澳]James Turnbull著

李兆海 刘斌 巨震 译

[本书网站](https://www.dockerbook.com)、[本书示例](https://github.com/jamtur01/dockerbook-code)

第1章 简介
----------

容器被称为“操作系统级虚拟化”，容器技术可以让多个独立的用户空间运行在同一台宿主机上。
而“管理程序虚拟化”（Hypervisor Virtualization，HV）通过中间层将一台或多台独立的机器虚拟运行于物理硬件之上。

正因为容器“客居”于操作系统，所以容器只能运行与底层宿主机相同或相似的操作系统。比如：Ubuntu之上可以运行RedHat，但是不能运行Windows。

相对于“管理程序虚拟化”，容器被认为是不安全的。而也有人认为“管理程序虚拟化”因为暴露了操作系统，而显得更不安全。

随着技术的发展，容器不再仅仅是单纯的运行环境。而更像是一个完整的宿主机。

容器有较小的开销，因此宿主机可以运行更多的容器。

但是容器本书比较复杂，不易安装，管理和自动化也很困难。Docker就是为改变这一切而生。

### 1.1 Docker简介

Docker的目标是要提供：

- 提供一个简单、轻量的建模方式：上手快、启动快、性能高

- 职责的逻辑分离：开发、测试、生产的一致性，保证了开发和运维之间的职责清晰

- 快速、高效的开发生命周期：缩短了开发、测试、部署、上线的周期

- 鼓励使用面向服务的架构：推荐（鼓励）单个容器只运行一个应用程序或进程，形成一个分布式的应用模型，在这种模型下，应用程序或服务都可以表示为一系列内部互联的容器。

### 1.2 Docker组件

![](contents/docker-architecture.svg)

- Docker客户端和服务端，也称为Docker引擎

![](contents/engine-components-flow.png)

Docker是一个客户端/服务端（C/S）架构程序。

Client端：命令行工具（CLI）

Server端：[REST API](https://docs.docker.com/engine/reference/api/docker_remote_api/) + 守护进程(Daemon Process)

- Docker镜像：可以把镜像当作容器的“源代码”。镜像是Docker生命周期中的构建或打包阶段。

- Registry：可以使用公共的Registry——[Docker Hub](https://docs.docker.com/docker-hub/)，也可以架设自己的私有Registry。

- 容器：容器是Docker生命周期中的启动或执行阶段。

Docker借鉴了标准集装箱的概念，唯一不同的是：集装箱运输货物，而Docker运输软件。

> 补充阅读：《[Docker Overview](https://docs.docker.com/engine/understanding-docker/)》

### 1.3 能用Docker做什么

- 加速本地开发和构建的流程，使其更加高效、更加轻量化。

- 能够让独立服务或应用程序在不同的环境中，得到相同的运行结果。这一点在面向服务的架构和重度依赖微型服务的部署中尤其实用。

- 用Docker创建隔离的环境来进行测试。

- Docker可以让开发者先在本机构建一个复杂的程序或架构进行测试。

- 构建一个多用户的平台即服务（PaaS）基础设施。

- 提供独立的沙盒环境。

- 提供软件即服务（SaaS）应用程序。

- 高性能、超大规模的宿主机部署。

### 1.4 Docker与配置管理

Docker一个显著的特点就是，对不同的宿主机、应用程序和服务，可能会表现出不同的特性与架构。

在未来的一段时间内，Docker这种理想化的工作负载可能会与传统的基础设备部署共存一段时间。在绝大多数的组织中，Docker和配置管理工具可能都需要部署。

### 1.5 Docker的技术组件

- 一个原生的Linux容器格式，Docker中成为libcontainer

- Linux内核的命名空间（[namespaces](http://lwn.net/Articles/531114/)），用于隔离文件系统、进程和网络。

- 进程隔离：每个容器都运行在自己的进程环境中。

- 网络隔离：容器间的虚拟网络接口和IP地址都是分开的。

- 资源隔离和分组：使用[cgroups](https://en.wikipedia.org/wiki/Cgroups)（即control group，Linux的内核特性之一）将CPU和内存之类的资源独立分配给每个Docker容器。

- [写时复制](https://en.wikipedia.org/wiki/Copy-on-write)：文件系统都是通过写时复制创建的，也就意味着文件系统是分层的、快速的，而且占用的磁盘空间更小。

- 日志：容器产生的STDOUT、STDERR和STDIN这些IO流都会被收集并记入日志，用来进行日志分析和故障排错。

- 交互式shell：用户可以创建一个伪tty终端，将其连接到STDIN，为容器提供一个交互式的shell。

### 1.6 本书的内容

作者将全面讲解并演示Docker。

第2章 安装Docker
---------------

本节主要以Docker的安装为主，讲解了各种常见Linux发行版的安装以及使用[Docker Toolbox](https://www.docker.com/products/docker-toolbox)在OS X和Windows上的安装。

Docker安装的先决条件是：

- 64位CPU构架的计算机（目前只能是x86_64和amd64），不支持32位。可以用Linux命令`uname -a`查看。

- 运行Linux 3.8或更高版本内核。

- 内核必须支持一种适合的存储驱动（storage driver）

- 内核必须支持并开启[cgroups](https://en.wikipedia.org/wiki/Cgroups)和命名空间（[namespaces](http://lwn.net/Articles/531114/)）功能。

至于具体的安装步骤，书中说的并没有Docker安装文档详细，建议直接查看[Docker官方文档](https://docs.docker.com/engine/installation/)。

第3章 Docker入门
---------------

> 《[Docker命令行参考文档](https://docs.docker.com/engine/reference/commandline/cli/)》

```
parallels@ubuntu:~$ sudo docker run -i -t ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
952132ac251a: Pull complete 
82659f8f1b76: Pull complete 
c19118ca682d: Pull complete 
8296858250fe: Pull complete 
24e0251a0e2c: Pull complete 
Digest: sha256:f4691c96e6bbaa99d99ebafd9af1b68ace2aa2128ae95a60369c506dd6e6f6ab
Status: Downloaded newer image for ubuntu:latest
root@019b21d670f7:/#
```

命令解释：docker run

- -i：保证容器中的STDIN是开启的。

- -t：告诉Docker为要创建的容器分配一个伪tty终端。

- ubuntu：镜像的名字

- /bin/bash：启动容器后执行的语句

可以使用`docker ps -a`查看当前系统中容器的列表。

```
parallels@ubuntu:~$ docker ps -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED              STATUS                        PORTS               NAMES
87a430a359ef        ubuntu                "/bin/bash"              About a minute ago   Exited (0) 11 seconds ago                         ubuntu-web-001
```

```
docker run -i -t --name ubuntu-web-001 ubuntu /bin/bash
```

使用`--name`可以指定一个容器名称。

可以使用`docker start [container-name]`启动服务，类似的还有`docker stop`、`docker restart`、`docker create`

```
sudo docker start ubuntu-web-001 
```
也可以使用Container ID启动
```
parallels@ubuntu:~$ docker start 87a430a359ef597af9da14dcfc77290b35d8e1b5ccde6756f326f05efd458b0f 
87a430a359ef597af9da14dcfc77290b35d8e1b5ccde6756f326f05efd458b0f
parallels@ubuntu:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
87a430a359ef        ubuntu              "/bin/bash"         5 minutes ago       Up 13 seconds                           ubuntu-web-001
```

可以使用`docker attach`附着到已经启动的容器上。

```
docker attach ubuntu-web-001
```

交互式的容器用`docker run`之后会启动，用`exit`后，就退出，状态为关闭，用`docker start`后，会重新启动，但是不进入交互式界面，此时就可以使用`docker attach`命令进入。

与交互式容器不同，守护式容器可以用-d来指定。它不会将当前的命令提示符切换到docker容器中。

```
parallels@ubuntu:~$ docker run --name daemon_dave -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
8fbd7e9720089b647e8a70e974d0e541e1b3050375c75d148af9321ae8b85b79
```

使用`docker logs daemon_dave`可以查看容器的日志，但是是一次性的。`docker logs daemon_dave -f`增加了`-f`参数，类似于`tail -f`命令，可以监控Docker的日志。

```
parallels@ubuntu:~$ docker logs daemon_dave -f
hello world
hello world
hello world
hello world
hello world
```
增加`-t`参数可以增加时间
```
parallels@ubuntu:~$ docker logs daemon_dave -f -t
2016-08-28T15:49:41.292969746Z hello world
2016-08-28T15:49:51.293822132Z hello world
2016-08-28T15:50:01.295697278Z hello world
2016-08-28T15:50:11.297390260Z hello world
2016-08-28T15:50:21.299265255Z hello world
```
增加`--tail 0`可以查看最新的日志，增加`--tail 10`可以查看最新10条日志。

可以使用`--log-driver="syslog"`将默认的`json-file`日志驱动换掉，这将导致`docker logs`命令不再有效，日志将被重定向到syslog中。

同样地，还可以使用`--log-driver="none"`关闭日志。

使用`docker top daemon_dave`可以查看容器内的进程。

可以用`docker stats`查看容器的统计信息。

```
CONTAINER           CPU %               MEM USAGE / LIMIT    MEM %               NET I/O             BLOCK I/O           PIDS
2945eb23b5a4        0.10%               328 KiB / 5.74 GiB   0.01%               4.383 kB / 648 B    0 B / 0 B           0
```

使用`docker exec -d daemon_dave touch /etc/volnet_config`可以在容器内执行一个不需要交互的命令。

使用`docker exec -i -t daemon_dave ls /etc ｜ grep volnet`可以在容器内执行一个需要交互的命令。

`docker stop`和`docker kill`的区别在于，前者发送SIGTERM信号，后者发送SIGKILL信号。

使用`docker run --restart=always ……`等命令可以保持在容器停止后重启，具体的参数详见[run reference --restart](https://docs.docker.com/engine/reference/run/#restart-policies-restart)。

使用`docker inspect ubuntu-web-001`命令，可以获得容器的更多信息。

```
parallels@ubuntu:~$ docker inspect --format='{{ .State.Running }}' ubuntu-web-001
false

parallels@ubuntu:~$ docker inspect --format='{{ .NetworkSettings.IPAddress }}' ubuntu-web-001
172.17.0.2
```
目录`/var/lib/docker`存放着Docker镜像、容器以及容器的配置。
```
parallels@ubuntu:~$ sudo ls /var/lib/docker
[sudo] password for parallels: 
aufs  containers  graph  image	linkgraph.db  network  repositories-aufs  swarm  tmp  trust  volumes
```

使用`docker rm`删除单个容器（不包括运行中的），`docker rm -f`删除单个容器（包括运行中的）

使用下面语句删除所有容器：

```
sudo docker rm `sudo docker ps -a -q`
```
以上命令中，`-q`标志表示只需要返回容器的ID而不会返回容器的其它信息。这样我们就得到了容器ID的列表，并传给了`docker rm`命令，从而达到删除所有容器的目的。

第4章 使用Docker镜像和仓库
-----------------------

### 4.1 什么是Docker镜像

[官方文档](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/#understand-images-containers-and-storage-drivers)

从底向上：
    
    bootfs（引导文件系统）（只读，启动后从内存中移除）
    
    -> rootfs（root文件系统，可以是一种或多种操作系统（如Debian或者Ubuntu文件系统））（只读，在传统Linux引导过程中，root文件系统最先会以只读的方式加载，当引导结束并完成了完整性检查之后，它才会被切换为读写模式。），延伸阅读：[Union Mount](https://en.wikipedia.org/wiki/Union_mount)

    -> 其它镜像（Apache、emacs等）

    -> 可写容器（Container Layer(R/W)）

顶层的可写容器，采用了写时复制（copy on write）

![](contents/sharing-layers.jpg)

### 4.2 列出镜像

列出Docker镜像：

```
sudo docker images
```

使用`docker run`命令的时候，如果镜像不存在，则默认会从官方的Registry中获取，也就是Docker Hub。

- Docker Hub：官方的Registry

- Docker Trusted Registry：可以运行在公司防火墙内部的产品，之前被称为“Docker Enterprise Hub”。[官方文档](https://docs.docker.com/docker-trusted-registry/)|[安装文档](https://docs.docker.com/docker-trusted-registry/install/)

### 4.3 拉取镜像

使用`sudo docker pull volnet/helloworld:1.0`可以只拉取镜像，不运行。其中，`volnet`是用户名，`helloworld`是仓库名，而`1.0`是TAG。如果镜像是由Docker官方提供的或者是合作厂商提供的，则没有“用户名”。

默认如果不指定TAG则拉取`TAG=lastest`的镜像。

### 4.4 查找镜像

使用`sudo docker search helloworld`查找所有Docker Hub上的镜像。

第5章 在测试中使用Docker
---------------------

第6章 使用Docker构建服务
---------------------

第7章 Docker编配和服务发现
-----------------------

第8章 使用Docker API
-------------------

第9章 获得帮助和对Docker进行改进
----------------------------