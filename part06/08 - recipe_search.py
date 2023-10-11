
def organize_into_lists(file : str):
    d = {"foodItem": [], "prepTime": [], "ingredients": []}
    timeFlag = 0
    
    with open (file) as myFile:
        temp = []
        for line in myFile:
            line = line.strip()
            if line.lower() != line:
                d["foodItem"].append(line)
                timeFlag = 1
                continue
            elif timeFlag:
                d["prepTime"].append(int(line))
                timeFlag = 0
                continue
            
            if line != "":
                temp.append(line)
            else:
                d["ingredients"].append(temp)
                temp = []

        d["ingredients"].append(temp)
    return(d)

def search_by_name(filename: str, word: str):
    d = organize_into_lists(filename)
    temp = []
    for w in d["foodItem"]:
        if word.lower() in w.lower():
            temp.append(w)
    return(temp)

def search_by_time(filename: str, prep_time: int):
    d = organize_into_lists(filename)
    temp = []
    for i in range(len(d["prepTime"])):
        if d["prepTime"][i] <= prep_time:
            item1 = d["foodItem"][i]
            item2 = d["prepTime"][i]
            temp.append(f"{item1}, preparation time {item2} min")
    return(temp)

def search_by_ingredient(filename: str, ingredient: str):
    d = organize_into_lists(filename)
    temp = []
    for i in range(len(d["foodItem"])):
        if ingredient in d["ingredients"][i]:
            item1 = d["foodItem"][i]
            item2 = d["prepTime"][i]
            temp.append(f"{item1}, preparation time {item2} min")
    return(temp)

def main():
    print(search_by_name("recipes1.txt", "cake"))
    print(search_by_time("recipes1.txt", 50))
    print(search_by_ingredient("recipes1.txt", "eggs"))

