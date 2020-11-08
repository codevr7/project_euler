n = int(input("Type in a number: "))
m = int(input("Type in another number: "))
for i in range(m, 1, -1):
    if m % i == 0:
        if n % i == 0:
            print(i)
            break
