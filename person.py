class Person:
    def __init__(self,name,id,email):
        self.name = name
        self.id = id
        self.email=email
    def identify(self):
        print(f"My name is {self.name},my badge number is {self.id}.")
class Employee(Person):
    def __init__(self,name,id,email,projectId):
        super().__init__(name,id,email)
        self.projectId=projectId
    def identify(self):
        print(f"my name is {self.name} and I am working on project Id:{self.projectId}")
class Manager(Person):
    def __init__(self,name,id,email,max_EmpManaged):
        super().__init__(name,id,email)
        self.max_EmpManaged=max_EmpManaged
        self.employee=[]
        #print(self.employee)
    def identify(self):
         print(f"I am {self.name} and I manage team consisting of {len(self.employee)} employees ")
              
    
    def addEmp(self,employee):
        if len(self.employee)<self.max_EmpManaged:
            self.employee.append(employee)
            return True
        return False



p1=Person("Todd",1,"T.email.com")
e1=Employee("Tim",2,"t.email",0)
e2=Employee("Rim",3,"r.email",0)
e3=Employee("Bim",4,"b.email",1)
e4=Employee("Kim",5,"k.email",1)
m1=Manager("Boss",10,"bo.email.com",3)
print(m1.addEmp(e1))
print(m1.addEmp(e2))
print(m1.addEmp(e3))
print(m1.addEmp(e4))
print(p1.identify())
print(e1.identify())
print(m1.identify())