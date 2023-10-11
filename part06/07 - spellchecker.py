if True:
    txt = input("Write text: ")
else:
    txt = "This is acually a good and usefull program"

wrds = txt.split(' ')
res = ""

with open("src/wordlist.txt") as words:
    dictionary = []
    for line in words:
        line = line.strip()
        dictionary.append(line)
    for i in wrds:
        if i.lower() in dictionary:
            res += i + " "
        else:
            res += "*" + i + "* "
print(res)