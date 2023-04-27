counter = 1

while True:
    pin = int(input("PIN: "))
    if (pin != 4321):
        print("Wrong")
        counter += 1
    else:
        if counter == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print("Correct! It took you " + str(counter) + " attempts")
        break