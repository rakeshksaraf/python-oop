class Dog:
    def __init__(self,who):
        self.ron=who
        print(self.ron)
    def bark(self):
        print("woof") 
    def legs(self,x):
        return x
d1= Dog("ruby")
print(type(d1))
d1.bark()
print(d1.legs(4))
