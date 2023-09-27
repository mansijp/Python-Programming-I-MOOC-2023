def length_of_longest (myList: list):
    longest = ""
    for i in myList:
        if len(i) > len(longest):
            longest = i
    return len(longest)

if __name__ == "__main__":
    length_of_longest(["first", "second", "fourth", "eleventh"])