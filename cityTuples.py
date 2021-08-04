cityNames=['Detroit','Aan Arbor','Pittsburg','Mars','New York']
populations= [200,400,2000,10,10000]
states=['MI','MI','PA','PA','NY']

cityTuples= zip(cityNames,populations,states)
#print(list(cityTuples))

class City:
    def __init__(self,cityName,populations,states):
        self.cityName=cityName
        self.populations=populations
        self.states=states
    def __str__(self):
         return f"{self.cityName},{self.populations},{self.states}"
    #def printName(self):
        #return f"{self.cityName},{self.populations},{self.states}"
        #print(f"{self.cityName},{self.populations},{self.states}")
cities =[]
for city_tup in cityTuples:
    name,pop,state= city_tup
    #print(name,pop,state)
    city=City(name,pop,state)
    cities.append(city)
#     #print(city_tup)
    #print(city)
    #print(city.printName())
# cities= [City(n,p,s) for (n,p,s) in cityTuples]
print(cities)

# cities= [City(*t) for t in cityTuples]
# # for t in cities:
# #     print(t)
# print(cities)

