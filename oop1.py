class Dog:
    def __init__(self,name):
        self.name=name
        print(name)
    def bark(self):
        print("woof") 
    def legs(self,x):
        return x
    def eat(self, food):
	return food
d1= Dog("ruby")
print(type(d1))
d1.bark()
print(d1.legs(4))
print(d1.food("bone"))
