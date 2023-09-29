def remove_smallest(numbers: list):
    return(numbers.remove(min(numbers)))

def main():
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)