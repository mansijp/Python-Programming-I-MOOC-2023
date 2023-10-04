def create_tuple(x: int, y: int, z: int):
    tuple =  (min([x, y, z]), max([x, y, z]), sum([x, y, z]))
    return (tuple)

def main():
    print(create_tuple(5, 3, -1))
