n = int(input("Please type in a number: "))
j = n

for i in range(1, (n//2)+1):
    print (i)
    print (j)
    j -= 1

if (n%2 == 1):
    print(n//2 + 1)