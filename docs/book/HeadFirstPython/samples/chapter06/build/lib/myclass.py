class MyClass:
    NickName = ''
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def GetName(self):
        return self.Name + '(' + self.NickName + ')'

    def GetAge(self):
        return self.Age

    def AddAge(self, age):
        self.Age += age
        return self.Age

class MyClass2(MyClass):
    def __init__(self, name):
        MyClass.__init__(self, name, 20)

    def AddAge(self, age):
        self.Age += (2 * age)
        return self.Age

obj1 = MyClass('Eric', 18)
obj2 = MyClass2('Volnet')

# Eric 18
print(obj1.GetName() + '-' + str(obj1.GetAge()))
# Volnet 20
print(obj2.GetName() + '-' + str(obj2.GetAge()))

obj1.AddAge(10)
# Eric 18+10=28
print(obj1.GetName() + '-' + str(obj1.GetAge()))

obj2.AddAge(10)
# Volnet 20+2*10=40
print(obj2.GetName() + '-' + str(obj2.GetAge()))

obj1.Name = 'Eric Kung'
obj1.NickName = 'volnet'
# Eric Kung(volnet) 18+10=28
print(obj1.GetName() + '-' + str(obj1.GetAge()))
# Volnet 20
print(obj2.GetName() + '-' + str(obj2.GetAge()))