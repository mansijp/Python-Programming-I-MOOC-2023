
def distinct_numbers(myList : list):
    magnitude = []
    for i in range(min(myList), max(myList)+1):
        if (i in myList) and (not(i in magnitude)):
            print("works")
            magnitude.append(i)
    return(magnitude)

if __name__ == "__main__":
    distinct_numbers([3, 2, 2, 1, 3, 3, 1])
