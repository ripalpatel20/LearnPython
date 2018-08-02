class Parent():
    def __init__(self):
        print("this is parent class")
    def parentfunc(self):
        print("this is parent function")

#p = Parent()
#print(p.__init__())
#print(p.parentfunc())


class Child(Parent):
    def __init__(self):
        print("this is child class")
    def childfunc(self):
        print("this is child function")
c = Child()
#print(c.__init__())
print(c.childfunc())
print(c.parentfunc())