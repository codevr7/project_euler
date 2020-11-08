a = int(input("Type in a number: "))
b = int(input("Type in another number: "))
# Taking two inputs
for i in range(1,b + 1):
    val = a*i  
    if val % b == 0:
        print (a*i)
        break
