import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distance_origin(self):
        d=(self.x**2+self.y**2)**.5
        return d
    def distance(self,p2):
        return (round(math.sqrt((self.x-p2.x)**2-(self.y-p2.y)**2),2))
p1=Point(4,3)
p2=Point(2,2)
print(p1.x)
print(p1.distance_origin())
print(p1.distance(p2))