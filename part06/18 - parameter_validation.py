def new_person(name: str, age: int):
    if (name == ""):
        raise ValueError("The name is an empty string")
    elif(len(name.split(' ')) < 2):
        raise ValueError("Name cannot have less than 2 words")
    elif(len(name) > 40):
        raise ValueError("Name cannot be more than 40 characters")
    elif(age < 0):
        raise ValueError("Age cannot be less than 0")
    elif(age > 150):
        raise ValueError("Age cannot be more than 150")
    else:
        tup = (name, age)
        return (tup)

def main():
    print(new_person("", 10))