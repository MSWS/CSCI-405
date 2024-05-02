cities = [1,     9,    88,    150,   249,   250,  300,   400,   500,   550,  600, 601 ,  700,  800, 900,   1000]
infected=[False, True, False, False, False, True, False, False, False, False,True,False, False,False,False,False]

c = []

def get_city(i):
    if i == 1:
        return 1
    if len(c) > i:
        return c[i]
    n = len(cities)
    farthestDist = -1
    farthestCity = -1
    for j in range(i, n):
        if infected[j]:
            continue
        if cities[j] - cities[get_city(i - 1)] > 100:
            break
        dist = cities[j] - cities[get_city(i - 1)]
        if dist > farthestDist:
            farthestDist = dist
            farthestCity = j
    if farthestCity == -1:
        raise Exception("No city found")
    c.append(farthestCity)
    return farthestCity

current = 0
while current < len(cities)-1:
    current = get_city(current + 1)
    print(current)

print(c)
print(", ".join(map(lambda s: str(s+1), c)))
print(", ".join(map(lambda s: str(cities[s]), c)))