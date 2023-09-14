def line(n, text):
    if len(text) >=1:
        print(text[0]*n)
    else:
        print("*"*n)
                
def square(size, character):
    for i in range(size):
        line(size, character)

if __name__ == "__main__":
    square(5, "x")