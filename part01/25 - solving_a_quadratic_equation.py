from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

print("The roots are " + str((-1*b+sqrt(b*b-4*a*c))/(2*a)) + " and " + str((-1*b-sqrt(b*b-4*a*c))/(2*a)))