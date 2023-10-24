# from random --> import randint, shuffle, choice

from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    lottery = []
    for i in range(amount):
        n = randint(lower, upper)
        while (n in lottery):
            n = randint(lower, upper)
        lottery.append(n)
    lottery.sort()
    return (lottery)

def main():
    print(lottery_numbers(9, 1, 15))
    for number in lottery_numbers(7, 1, 40):
        print(number)

