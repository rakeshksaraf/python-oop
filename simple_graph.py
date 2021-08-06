class Point:
    
    printedRep='*'
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def graph(self):
        rows=[]
        size=max(int(self.x),int(self.y))+2
        for j in range(size-1):
            if j+1 ==self.y:
                rows.append(str((j+1)%10) + (" "*(int(self.x)-1))+self.printedRep)
            else:
                rows.append(str(j+1%10))
        rows.reverse()
        x_axis=''
        for i in range(size):
            x_axis+=(str(i%10)) # modulus creates axis 01234567890123, where second zero =10 and second 1=11
        rows.append(x_axis)

        return "\n".join(rows)
p1=Point(2,3)
print(p1.graph())
