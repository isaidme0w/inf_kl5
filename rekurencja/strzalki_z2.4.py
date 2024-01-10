# Iteracyjnie
def czyDojdzie(n):
    a = int(n[0])
    b = int(n[1])

    while b > a:
        if b % 2 != 0:
            b -= 1
        b /= 2
    
    if b == a:
        return True
    return False

# Rekurencyjnie
def czyDojdzieRek(a, b):
    if b <= a:
        if b == a:
            return True
        return False
    else:
        if b % 2 != 0:
            b -= 1
        return czyDojdzieRek(a, b / 2)

file = open('pary.txt', 'r+')
content = file.readlines()

for line in content:
    line = line.replace("\n", "")
    line = line.split(" ")
    a = int(line[0])
    b = int(line[1])
    if czyDojdzieRek(a, b):
        print(line[0], line[1])

file.close()