str1 = input("Please type in string 1: ")
str2 = input("Please type in string 2: ")

if len(str1) > len(str2):
    print(str1 + " is longer")
elif len(str2) > len(str1):
    print(str2 + " is longer")
else:
    print("The strings are equally long")