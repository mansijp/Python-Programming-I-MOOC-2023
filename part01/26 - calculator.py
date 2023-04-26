a = int(input("Number 1: "))
b = int(input("Number 2: "))
op = input("Operation: ")

if op == "add":
    print(f"{a} + {b} = {a+b}")
elif op == "subtract":
    print(f"{a} - {b} = {a-b}")
elif op == "multiply":
    print(f"{a} * {b} = {a*b}")