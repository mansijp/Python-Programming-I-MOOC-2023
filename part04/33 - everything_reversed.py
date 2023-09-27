def everything_reversed(myList : list):
    result = []
    for i in range(len(myList)-1, -1, -1):
        result.append(myList[i][::-1])
    return (result)