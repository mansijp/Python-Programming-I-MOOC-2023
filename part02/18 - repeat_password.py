pswd = input("Password: ")

while True:
    repeat = input("Repeat password: ")
    if (repeat != pswd):
        print("They do not match!")
    else:
        print("User account created!")
        break