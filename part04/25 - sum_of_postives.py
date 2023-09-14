def sum_of_positives(list: list):
    sum = 0
    for i in list:
        if i > 0:
            sum = sum + i
    return sum

if __name__ == "__main__":
    sum_of_positives([1, -1, 2, -2, 3, -3])