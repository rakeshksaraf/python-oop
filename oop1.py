class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
    def bark(self):
        print("woof") 

	
d1= Dog("ruby",10)
print(type(d1))
d1.bark()
print(d1.get_name())
print(d1.get_age())
d1.set_age(12)
print(d1.get_age())



