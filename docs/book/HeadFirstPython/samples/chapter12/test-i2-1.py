name = 'Head First Python'
def what_happen_here():

	print('1.' + name)
	
	name = name + ' is a great book!'
	
	print('2.' + name)

what_happen_here()
print('3.' + name)

"""
Traceback (most recent call last):
  File "/Users/volnet/volnet.github.io/docs/book/HeadFirstPython/samples/chapter12/test-i2-1.py", line 10, in <module>
    what_happen_here()
  File "/Users/volnet/volnet.github.io/docs/book/HeadFirstPython/samples/chapter12/test-i2-1.py", line 4, in what_happen_here
    print('1.' + name)
UnboundLocalError: local variable 'name' referenced before assignment
>>> 
"""
