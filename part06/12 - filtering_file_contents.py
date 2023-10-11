# removing files
    # import os
    # os.remove("unnecessary_file.csv")

def filter_solutions():
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()

    with open("correct.csv", "a") as correct:
        with open("incorrect.csv", "a") as incorrect:
            with open("solutions.csv") as file:
                for line in file:
                    line = line.strip()
                    temp = line.split(";")

                    if ("+" in temp[1]):
                        operation = temp[1].split('+')                        
                        if(int(operation[0]) + int(operation[1])) == int(temp[2]):
                            correct.write(line+"\n")
                        else:
                            incorrect.write(line+"\n")
                    
                    elif ("-" in temp[1]):
                        operation = temp[1].split('-')
                        if(int(operation[0]) - int(operation[1])) == int(temp[2]):
                            correct.write(line+"\n")
                        else:
                            incorrect.write(line+"\n")
                            
def main():
    filter_solutions()
