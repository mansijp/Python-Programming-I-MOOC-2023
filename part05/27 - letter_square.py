from string import ascii_lowercase

# assuming there would a max of only 26 layers
layers = int(input("Layers: "))

# Creating a dictionary with the alphabetical letters
alphabet = [*ascii_lowercase]
d = {}
for i in range(1, 27):
    d[i] = alphabet[i-1].upper()

# Body of code
result = []

for row in range(layers*2-1):
    temp = ""
    for col in range(layers*2-1):
        distance = dist = min(row, col, 2*layers-2-row, 2*layers-2-col)
        temp += d[layers - distance]  
    result.append(temp)

# Printing the result
for i in result:
    print(i)
