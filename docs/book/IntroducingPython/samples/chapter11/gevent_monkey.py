import gevent
from gevent import monkey; monkey.patch_all()
import socket
hosts=["www.github.com", "www.amazon.com"]
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)