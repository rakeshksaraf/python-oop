class Dog:
<<<<<<< HEAD
    def __init__(self,name):
        self.name=name
        print(name)
    def breed(self,which):
	return which
=======
    def __init__(self,name,age):
        self.name=name  
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
>>>>>>> 35b65ce (first class)
    def bark(self):
        print("woof") 
    def legs(self,x):
        return x
<<<<<<< HEAD
    def eat(self, food):
	return food
	return food
d1= Dog("ruby")
=======
d1= Dog("ruby",3)
>>>>>>> 35b65ce (first class)
print(type(d1))
d1.bark()
print(d1.get_name())
print(d1.get_age())
print(d1.legs(4))
<<<<<<< HEAD
print(d1.food("bone"))
print(d1.breed("husky"))
=======
d1.set_age(12)
print(d1.get_age())
>>>>>>> 35b65ce (first class)
