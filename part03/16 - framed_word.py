word = input("Word: ")

starsleft = (28-len(word)) // 2
starsright = 28 - starsleft - len(word)

print("*" * 30)
print("*" + " "*starsleft + word + " "*starsright + "*")
print("*" * 30)
