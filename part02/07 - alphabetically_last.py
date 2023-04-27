
s = input("Please type in the 1st word: ")
t = input("Please type in the 2nd word: ")

if s < t:
    print(t + " comes alphabeticaly last.")
elif t < s:
    print(s + " comes alphabetically last.")
else:
    print("You gave the same word twice.")