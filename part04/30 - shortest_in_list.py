def shortest(myList : list):
    shortest = myList[0]
    for i in myList:
        if len(i) < len(shortest):
            shortest = i
    return shortest

if __name__ == "__main__":
    shortest(["first", "second", "fourth", "eleventh"])