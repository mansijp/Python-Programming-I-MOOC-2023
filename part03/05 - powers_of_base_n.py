
upper = int(input("Upper limit: "))
base = int(input("Base: "))
exp = 0
i = pow(base, exp)

while i <= upper:
    print(str(i))
    exp += 1
    i = pow(base, exp)