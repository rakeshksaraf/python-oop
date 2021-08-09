from random import randrange,choice
import sys

class Pet:
    hunger_decrement=2
    boredom_decrement=3
    boredom_threshold=10
    hunger_threshold=10
    sounds=["wuh"]

    def __init__(self,name='defu'):
        self.name = name
        self.hunger=randrange(self.hunger_threshold)
        self.boredom=randrange(self.boredom_threshold)
        self.sounds=self.sounds[:] # copy the class attribute, so that when we make changes to it,
        # we won't affect the other Pets in the class
    def clock_tick(self):
        self.boredom+=1
        self.hunger+=1
    def mood(self):
        if self.boredom<=self.boredom_threshold and self.hunger<=self.hunger_threshold:
            return "happy"
        elif self.hunger>self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        return f" I am {self.name} and I am {self.mood}"

    def update_boredom(self):
        self.boredom=self.boredom-self.boredom_decrement
        return self.boredom
    def update_hunger(self):
        self.hunger=self.hunger-self.hunger_decrement
        return self.boredom
    def hi(self):
        print(choice(self.sounds()))
        self.update_boredom()
    def teach(self,word):
        self.sounds.append(word)
        self.update_boredom()
    def feed(self):
        self.update_hunger()
class Cat(Pet):
    sounds=["purr"]
    def __init__(self,name,fav_food):
        super().__init__(name)
        self.fav_food=fav_food

    def mood(self):
        if self.hunger<=self.hunger_threshold and self.boredom<=self.boredom_threshold:
            return "happy and I love you!"
        elif self.hunger>self.hunger_threshold:
            return f"Not Happy. Feed me {self.fav_food}"
        else:
            return "bored. Let's do something."
class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")
class Bird(Pet):
    sounds=["koo"]
    def __init__(self,name='cruso',chirp_num=2):
        super().__init__(name)
        self.chirp_num=chirp_num
    def hi(self):
        for i in range(self.chirp_num):
            print (self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

class Lab(Dog):
    def fetch(self):
        return "I found the tennis ball!"

    def hi(self):
        print(self.fetch())
        print(self.sounds[randrange(len(self.sounds))])

class Poodle(Dog):
    def dance(self):
        return "Dancin' in circles like poodles do."

    def hi(self):
        print(self.dance())
        Dog.hi(self)
def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)


    

    


    
