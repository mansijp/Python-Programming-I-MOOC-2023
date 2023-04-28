count = 0
sum = 0
pos = 0
neg = 0
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    num = int(input("Number: "))
    if(num == 0):
        break
    elif num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    count += 1
    sum += num

print("... the program asks for numbers")
print("Numbers typed in " + str(count))
print("The sum of the numbers is " + str(sum))
print("The mean of the numbers is " + str(sum/count))
print("Positive numbers " + str(pos))
print("Negative numbers " + str(neg))