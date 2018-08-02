class person:
    pass
    list = ["rp","patel"]
    def name(self):
        return "ripal"
    def age(self):
        return "31"
p = person()
print(p.list[0])
print(p.name())
print(p.age())


class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name

        def name(self):
            print("ripal")

        def age(self):
            print("31")

            p1 = Person()
            print(p1.list[0])
            print(p1.name())
            print(p1.age())