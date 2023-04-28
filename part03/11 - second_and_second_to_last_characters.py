string = input("Please type in a string: ")

second = string[1]
second_last = string[len(string) - 2]

if second == second_last:
    print("The second and the second to last characters are " + second)
else:
    print("The second and the second to last characters are different")