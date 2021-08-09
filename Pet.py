import random
class Pet:
    # instance variables:
    hunger_decrement=3
    boredom_decrement=6
    hunger_threshold=5
    boredom_threshold=10
    sounds=['Meh']

    def __init__(self,name='kitts'):
        self.name=name
        self.hunger=random.randrange(0, self.hunger_threshold)# random integer between 0 and threshold
        self.boredom=random.randrange(0,self.boredom_threshold) #int
        self.sounds=self.sounds[:] #copy list of strings, words taught to pet
    def clock_tick(self):
        self.hunger+=1
        self.boredom+=1
    def mood(self):
        if self.hunger>self.hunger_threshold and self.boredom>self.boredom_threshold:
            return "hungry and bored"
        if self.hunger>self.hunger_threshold and self.boredom<=self.boredom_threshold:
            return "hungry"
        if self.hunger<=self.hunger_threshold and self.boredom>self.boredom_threshold:
            return "bored"
        else:
            return "Feeling good!"
    def __str__(self):
        return f"I am {self.name} and I am {self.mood()}"

    def reduce_boredom(self):
        self.boredom= self.boredom-self.boredom_decrement
    def reduce_hunger(self):
        self.hunger= self.hunger-self.hunger_decrement
    def feed(self):
        self.reduce_hunger()

    def teach(self,word):
        self.sounds.append(word)
        self.reduce_boredom()
    def hi(self):
        self.reduce_boredom()
        print(random.choice(self.sounds))
p1=Pet("Ruby")

for i in range(10):
    p1.clock_tick()
    print(p1)
print(p1)
p1.teach("purr")
p1.teach("wow")
for i in range(10):
    p1.clock_tick()
for i in range(3):
    p1.hi()
p1.feed()
print(p1)

    



