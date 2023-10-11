
# opening the file in append mode

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    cmd = int(input("Function: "))
    if cmd == 0:
        print("Bye now!")
        break
    elif cmd == 1:
        text = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(f"{text}\n")
        print("Diary saved\n")
    elif cmd == 2:
        with open("diary.txt") as file:
            print("Entries:")
            print(file.read())
    
