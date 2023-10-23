def read_input(inputStr:str, num1:int, num2:int):
    while True:
        try:
            n = int(input(inputStr))
            if (n > num1 and n < num2) or (n < num1 and n > num2):
                return (n)
            else:
                raise (ValueError)
        except ValueError:
            print("You must type in an integer between", num1, "and", num2)

def main():
    number = read_input("Please type in a number: ", 15, 10)
    print("You typed in:", number)

#------Types of exceptions------
    # ValueError
    # TypeError
    # IndexError
    # ZeroDivisionError
    # FileNotFoundError, UnsupportedOperation, PermissionError