def line(n, text):
    if len(text) >=1:
        print(text[0]*n)
    else:
        print("*"*n)

def shape(num1, text1, num2, text2):
    for i in range(1, num1+1):
        line(i, text1)
    for i in range(1, num2+1):
        line(num1, text2)

if __name__ == "__main__":
    shape(5, "x", 2, "o")