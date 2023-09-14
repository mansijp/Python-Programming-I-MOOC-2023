def line(n, text):
    if len(text) >=1:
        print(text[0]*n)
    else:
        print("*"*n)

if __name__ == "__main__":
    line(5, "x")
