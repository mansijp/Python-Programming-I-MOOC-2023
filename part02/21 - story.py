s = ""
lastword = ""

while True:
    word = input("Please type in a word: ")
    
    if(word != "end" and word != lastword):
        s = s + word + " "
    else:
        print(s)
        break
    lastword = word

