def all_the_longest(myList : list):
    result = []
    longest = ""
    for i in myList:
        if len(i) >= len(longest):
            longest = i
    for i in myList:
        if len(i) == len(longest):
            result.append(i)
    return (result)

if __name__ == "__main__":
    all_the_longest(["first", "second", "fourth", "eleventh"])
        