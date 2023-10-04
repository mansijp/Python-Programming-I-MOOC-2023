
# assuming the same number will not be added again 
# for each person in the phonebook

book = {}
while True:
    cmd = int(input("command (1 search, 2 add, 3 quit): "))
    if cmd == 3:
        print("quitting...")
        break
    elif cmd == 2:
        name = input("name: ")
        num = input("number: ")
        if name in book:
            book[name].append(num)
        else:
            book[name] = [num]
        print("ok!")
    elif cmd == 1:
        name = input("name: ")
        if name in book:
            for i in book[name]:
                print(i)
        else:
            print("no number")