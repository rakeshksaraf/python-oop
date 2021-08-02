# class attribute and class method
## Could define a global attribute here
Gravity=-9.8
class Person:
    num_people=0 # class attribute
    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.num_people
    @classmethod
    def add_person(cls):
        cls.num_people += 1

p1=Person("tim")
p2=Person("Tones")
p3=Person("Bones")

print(p2.num_people)
#Person.num_people =8
print(p1.num_people)
print(Person.number_of_people())
#print(Person.num_people*Gravity)