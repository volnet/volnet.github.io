使用Docker运行ELK + Beat
===============================

如何运行
-------------------------------

1. 启动ElasticSearch & Kibana:

在宿主机上运行：

```
cd scripts/
./ek.sh
```

2. 测试ElasticSearch & Kibana:

在宿主机上运行：

```
curl http://0.0.0.0:9200
curl http://0.0.0.0:5601
```

或者在浏览器上打开它们.

3. 运行MetircBeat，可以测试ElasticSearch和Kibana。下面的例子将监控宿主机而不是docker内的linux的system info，并将它们发送到上面配置的ElasticSearch中:

```
./metricbeat.sh
docker ps
```

可以看到`metricbeat_test`容器正在运行，如果没有，就等一会儿再次运行它，可能因为ElasticSearch和Kibana的启动需要一定的时间，而这时候启动MetricBeat将导致失败。

4. 打开Kibana查看监控

浏览器访问`http://hostIP:5601`，点击左侧的Dashboard.

你将看到`metricbeat-*`相关的Tab，如果没有看到图表，或者图表为空，可能是选择的时间段有错。系统默认选择的是`Last 15 minutes`，但是可能因为虚拟机（特别是Windows的HyperV+Linux）中的时间不对。（可以参考[这里](../linux/system/utctime.md)）

5. [可选]如果你想要释放资源，删除数据，或者前面的步骤有错需要回到原点，可以尝试运行：

```
./resetall.sh
```

6. 同样的步骤可以运行filebeat：

```
./filebeat.sh
docker ps
```

相关资源
-------------------------------

1. 从Docker Hub官网下载ElasticSearch的Docker版本

```
docker pull elasticsearch
```

2. 从Docker Hub官网下载Kibana的Docker版本

```
docker pull kibana
```

3. 从docker.elastic.io下载MetricBeat的Docker版本，并从这篇文章开始：[Getting started with Metricbeat](https://www.elastic.co/guide/en/beats/metricbeat/current/metricbeat-getting-started.html)

```
docker pull docker.elastic.co/beats/metricbeat:6.3.0
```

4. 从docker.elastic.io下载FileBeat的Docker版本，并从这篇文章开始：[Getting Started With Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-getting-started.html)

```
docker pull docker.elastic.co/beats/filebeat:6.3.0
```

5. metricbeat.yml的配置示例

```
https://www.elastic.co/guide/en/beats/metricbeat/current/metricbeat-module-system.html
```

FAQ
-------------------------------

1. 出现权限不足的情况

因为docker中使用了用户1000来运行beat，但是启动docker的时候，默认是root，所以在读取/修改`--volume 卷`里的配置文件的时候，会遇到权限不足的问题。

方法1：

在宿主机上将对应目录/文件修改Owner即可。假设执行下面的语句会遭遇权限问题：

```
docker run -d -v "$PWD/logs/":/usr/share/filebeat/logs/ docker.elastic.co/beats/filebeat:6.3.0
```

在此之前在宿主机上需要运行：

```
chown -R 1000 $PWD/logs/
```

并且调整docker运行语句为：（注意有个 [:z](https://docs.docker.com/storage/bind-mounts/#configure-the-selinux-label) ）

```
docker run -d -v "$PWD/logs/":/usr/share/filebeat/logs/:z docker.elastic.co/beats/filebeat:6.3.0
```

方法2：

和方法1类似，只是将这个过程放到Dockerfile中，建立自定义的Dockerfile。