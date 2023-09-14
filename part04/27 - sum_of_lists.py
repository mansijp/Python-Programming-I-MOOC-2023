def list_sum(a:list, b:list):
    new = []
    for i in range(len(a)):
        new.append(a[i] + b[i])
    return new

if __name__ == "__main__":
    list_sum([1, 2, 3], [4, 5, 6])