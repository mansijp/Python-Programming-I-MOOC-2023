def oldest_person(people: list):
    year = []
    for i in people:
        year.append(i[1])
    index = year.index(min(year))
    return(people[index][0])

def main():
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    oldest_person(people)