from random import choice

def roll(die: str):
    if die == 'A':
        return(choice([3, 3, 3, 3, 3, 6]))        
    elif die == 'B':
        return(choice([2, 2, 2, 5, 5, 5]))
    elif die == 'C':
        return(choice([1, 4, 4, 4, 4, 4]))
    
def play(die1: str, die2: str, times: int):
    winner1 = 0
    winner2 = 0
    tie = 0
    for i in range(times):
        r = roll(die1)
        s = roll(die2)
        if r > s:
            winner1 += 1
        elif s > r:
            winner2 += 1
        else:
            tie += 1
    return((winner1, winner2, tie))

    
def main():
    parts = play('B', 'C', 100)
    print(parts[0])
    print(parts[1])
    print(parts[2])


        