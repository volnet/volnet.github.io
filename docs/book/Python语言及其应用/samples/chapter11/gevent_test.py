import gevent
from gevent import socket
hosts=["www.github.com", "www.amazon.com"]
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)