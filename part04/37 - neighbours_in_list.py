def longest_series_of_neighbours(myList : list):
    longest = 1
    result = 1
    for i in range(1, len(myList)):
        
        if abs(myList[i-1]-myList[i]) == 1:
            result += 1
        else:
            result = 1
        longest = max(longest, result)
    return (longest)