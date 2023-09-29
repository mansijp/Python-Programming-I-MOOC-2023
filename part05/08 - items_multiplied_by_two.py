def double_items(numbers: list):
    result = []
    for i in numbers:
        result.append(i*2)
    return (result)
    
def main():
    numbers = [2, 4, 5, 3, 11, -4]
    doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", doubled)