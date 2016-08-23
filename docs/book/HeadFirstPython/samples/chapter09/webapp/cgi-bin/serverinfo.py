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