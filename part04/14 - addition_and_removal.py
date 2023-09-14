# pop(index) removes item from list and returns value at index
# remove(value) finds the value and then removes the first occurrence

list = []
i = 1

while True:
    print(f"The list is now {list}")
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "x":
        print("Bye!")
        break
    elif action == "d":
        if (len(list) == 0):
            list.append(1)
        else:
            list.append(list[-1]+1)
    elif action == "r":
        list.remove(list[-1])

