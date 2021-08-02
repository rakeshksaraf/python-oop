class Person:
    num_people=0
    def __init__(self,name):
        self.name = name
p1=Person("tim")
p2=Person("Tones")

print(p2.num_people)
Person.num_people =8
print(p1.num_people)