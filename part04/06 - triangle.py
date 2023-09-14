def line(n, text):
    if len(text) >=1:
        print(text[0]*n)
    else:
        print("*"*n)

def triangle(size):
    for i in range(1, size+1):
        line(i, "#")

if __name__ == "__main__":
    triangle(5)
