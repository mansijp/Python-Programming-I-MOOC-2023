yr = int(input("Please type in a year: "))

if yr%4 == 0:
    if yr%100 == 0:
        if yr%400 == 0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That year is not a leap year.")