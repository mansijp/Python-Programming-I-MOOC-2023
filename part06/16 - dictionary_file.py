
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    cmd = int(input("Function: "))
    if cmd == 3:
        print("Bye!")
        break
    elif cmd == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        unique = True
        with open("dictionary.txt") as file:
            for line in file:
                line = line.strip("\n")
                if finnish == line[0: line.find(" ")]:
                    unique = False
            if unique:
                with open("dictionary.txt", "a") as file:
                    file.write(f"{finnish} - {english}\n")
                file.close()
                print("Dictionary entry added")
    elif cmd == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                line = line.strip("\n")
                if search in line:
                    print(line)