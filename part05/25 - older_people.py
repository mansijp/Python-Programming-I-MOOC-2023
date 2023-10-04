def older_people(people: list, year: int):
    selected = []
    for i in people:
        if i[1] < year:
            selected.append(i[0])
    return (selected)

def main():
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(older_people(people, 1979))
