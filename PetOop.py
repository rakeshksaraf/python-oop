
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age=age

    def show(self):
        print(f"I am {self.name},I am {self.age}")
    def speak(self):
        print("Shall I just say ") 

class Cat(Pet):

    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color      
    def speak(self):
        print("Meow!")

class Dog(Pet):
    def speak(self):
        print("Bark!")
class Fish(Pet):
    pass
p1= Pet("Tim",19)
p1.show()
c1=Cat("Bill",34)
c1.show()
c1.speak()
f1=Fish("Bub",2)
f1.speak()