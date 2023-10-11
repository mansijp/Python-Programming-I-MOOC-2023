import math

def get_station_data(filename: str):
    d = {}
    with open(filename) as file:
        next(file)
        for line in file:
            line = line.strip()
            temp = line.split(';')
            tup = (float(temp[0]), float(temp[1]))
            d[temp[3]] = tup
    return(d)

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return(distance_km)

def greatest_distance(stations: dict):
    dis = {}
    for i in stations:
        for j in stations:
            dis[distance(stations, i, j)] = (i, j)
    greatest = max(dis)
     
    return((dis[greatest][0], dis[greatest][1], greatest))

def main():
    print(distance(get_station_data("stations1.csv"), "Designmuseo", "Hietalahdentori"))
    print(greatest_distance(get_station_data("stations1.csv")))

