import fractions

def fractionate(amount: int):
    res = []
    for i in range(amount):
        res.append(fractions.Fraction(1, amount))
    
    return (res)

def main():
    for p in fractionate(5):
        print(p)
    print()
    print(fractionate(5))