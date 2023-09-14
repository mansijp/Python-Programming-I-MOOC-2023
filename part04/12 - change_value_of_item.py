list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1:
      break
    val = int(input("New value: "))
    list[index] = val
    print(list)