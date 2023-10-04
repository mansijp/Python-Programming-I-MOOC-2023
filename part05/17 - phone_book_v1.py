
book = {}
while True:
    cmd = int(input("command (1 search, 2 add, 3 quit): "))
    if cmd == 3:
        print("quitting...")
        break
    elif cmd == 2:
        name = input("name: ")
        num = input("number: ")
        book[name] = num
        print("ok!")
    elif cmd == 1:
        name = input("name: ")
        if name in book:
            print(book[name])
        else:
            print("no number")