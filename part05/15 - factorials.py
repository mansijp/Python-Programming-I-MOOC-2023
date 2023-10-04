def factorials(n : int):
    f = {}
    temp = 1
    for i in range(1, n+1):
        temp *= i
        f[i] = temp
    return(f)

def main():
    print(factorials(5))
