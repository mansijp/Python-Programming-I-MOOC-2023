def find_words(search_term: str):
    temp = []
    if "." not in search_term and "*" not in search_term:
        with open("words.txt") as file:
            for line in file:
                line = line.strip("\n")
                if (line.startswith(search_term)):
                    return ([line])
                
    elif ("." in search_term and not "*" in search_term):
        with open("words.txt") as file:
            for line in file:
                line = line.strip("\n")
                if (len(line) == len(search_term)):
                    l = True
                    for j in range(len(search_term)):
                        if search_term[j] != line[j] and search_term[j] != ".":
                            l = False
                    if l:
                        temp.append(line)
        return(temp)
        
    elif("*" in search_term and "." not in search_term):
        i = search_term.find("*")
        if search_term.startswith("*"):  
            with open("words.txt") as file:
                for line in file:
                    line = line.strip("\n")
                    if (line.endswith(search_term[i+1:])):
                        temp.append(line)
        elif search_term.endswith("*"):
            with open("words.txt") as file:
                for line in file:
                    line = line.strip("\n")
                    if (line.startswith(search_term[:i])):
                        temp.append(line)
        return(temp)
                
def main():
    print(find_words("a...e"))
