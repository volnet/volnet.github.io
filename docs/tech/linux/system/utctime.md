系统时间不同步
==========================

> 适用于：CentOS

如果你需要使用互联网同步你的服务器时间，可以尝试下面的方法。（可能因为你使用了Windows的HyperV，而它的默认配置将导致所运行的CentOS运行在错误的时间上）

```
$ yum install ntp
$ systemctl start ntpd 
$ ntpdate time.nist.gov
$ systemctl enable ntpd
```

参考：https://www.jb51.net/os/RedHat/262058.html