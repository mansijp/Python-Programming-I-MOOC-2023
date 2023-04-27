year = int(input("Year: "))
yr = year + 1

while True:
    if yr%4 == 0:
        if yr%100 == 0:
            if yr%400 == 0:
                print(f"The next leap year after {year} is {yr}")
                break
            else:
                yr += 1
        else:
            print(f"The next leap year after {year} is {yr}")
            break
    else:
        yr += 1