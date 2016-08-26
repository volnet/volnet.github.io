name = 'Head First Python'
def what_happen_here():
    print('1.' + name)
    global name
    name = name + ' is a great book!'
    print('2.' + name)
what_happen_here()
print('3.' + name)

"""
1.Head First Python
2.Head First Python is a great book!
3.Head First Python is a great book!
"""