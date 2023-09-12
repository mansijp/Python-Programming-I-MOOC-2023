num = int(input("Please type in a number: "))

for i in range(1, (num//2)+1):
    print(2*i)
    print(2*i-1)

if(num%2 == 1):
    print(num)