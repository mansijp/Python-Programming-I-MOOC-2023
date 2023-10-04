def dict_of_numbers():
    numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    for i in range (21, 100):
        if i%10 > 0:
            remainder = i%10
            num = i - remainder
            numbers[i] = numbers[num] + "-" + numbers[remainder]
    return(numbers)

def main():
    dict_of_numbers()
