class Cereal:
    def __init__(self,name,brand,fiber):
        self.name=name
        self.brand=brand
        self.fiber=fiber
    def getF(self):
        return self.fiber
    #def __str__(self):
        #return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"
    # def __add__(self,otherCereal):
    #     return (self.fiber+otherCereal.fiber)
    # def sort_priority(self):
    #     return self.fiber
c1=Cereal("Corn Flakes","Kellogg's",9)
print(c1.name)
c2=Cereal("Honey Nut Cheerios","General Mills",3)
c3= Cereal("Bran","Korm",7)
print(c3.getF())
print(Cereal.getF)
print(c1)
print(c2)
L=[c1,c2,c3]
#print(c1+c2)
# for f in sorted(L,key=Cereal.sort_priority,reverse=True):
#     print(f.name)

for f in sorted(L,key=Cereal.getF,reverse=True):
    print(f.name)
for f in sorted(L,key=lambda x:x.getF()):
    print(f.name)