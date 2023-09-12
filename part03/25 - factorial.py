factorial = 1
num = int(input("Please type in a number: "))

while True:
    if num <= 0:
        break
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"The factorial of the number {num} is {factorial}")
    num = int(input("Please type in a number: "))
    factorial = 1
print("Thanks and bye!")