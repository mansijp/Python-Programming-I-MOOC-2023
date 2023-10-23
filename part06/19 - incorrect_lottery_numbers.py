def filter_incorrect():
    open('correct_numbers.csv', 'w').close()
    with open('correct_numbers.csv', 'a') as correct:
        with open("lottery_numbers.csv") as numbers:
            for line in numbers:
                line = line.strip("\n")
                tup = ((line.split(';'))[0], (line.split(';'))[1])

                # check tup[0]
                try:
                    n = int((tup[0].split('week '))[1]) + 1
                except:
                    continue

                # check tup[1]
                temp = tup[1].split(',')
                d = {}
                try:
                    for i in temp:
                        n = int(i)
                        if n < 1 or n > 39:
                            raise (ValueError)
                        d[n] = 0
                except ValueError:
                    continue
                if (len(d) != 7):
                    continue

                correct.write(line + "\n")

def main():
    filter_incorrect()

main()
