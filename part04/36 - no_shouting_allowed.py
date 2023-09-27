def no_shouting(myList : list):
    newList = []
    for i in myList:
        if not i.isupper():
            newList.append(i)
    return (newList)