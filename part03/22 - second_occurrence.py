string = input("Please type in a string: ")
sub = input("Please type in a substring: ")

if string[string.find(sub)+3:].find(sub) != -1:
    print (f"The second occurrence of the substring is at index {string[string.find(sub)+3:].find(sub) + string.find(sub)+3}.")
else:
    print("The substring does not occur twice in the string.")