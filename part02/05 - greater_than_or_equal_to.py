a = int(input("Please type in the first number: "))
b = int(input("Please type in another number: "))

if a > b:
    print("The greater number was: " + str(a))
elif b > a:
    print("The greater number was: " + str(b))
elif a == b:
    print("The numbers are equal!")