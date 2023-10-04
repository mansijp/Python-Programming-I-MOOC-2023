def histogram(string : str):
    words = {}
    for i in string:
        if i not in words:
            words[i] = 1
        else:
            words[i] += 1
    
    for i in words:
        print(i + " ", end="")
        print("*" * words[i])

def main():
    histogram("statistically")