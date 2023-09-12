word = input("Please type in a word: ")
char = input("Please type in a character: ")
output = ""

for i in range(len(word)):
    j = word.find(char)
    if j!=-1 and (j+2) < len(word):
        for k in range(3):
            output += word[j+k]
        break
print( output )

## Model solution ##

# index = word.find(character)
# if index!=-1 and len(word)>=index+3:
#     print(word[index:index+3])