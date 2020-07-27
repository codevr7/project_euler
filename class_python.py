class Commute:
    def __init__(self,val):
        self.val = val
    def __add__(self,other):
        print("running Add")
        if isinstance(other,Commute):
            print("isinstance True")
        return Commute(self.val + other)
    def __radd__(self,other):
        print("running Radd")
        return Commute(other + self.val)
    def __str__(self):
       print("Printing") 
       return str(self.val)

x = Commute(5)
y = Commute(10)
print(x)
print(14 + x)


