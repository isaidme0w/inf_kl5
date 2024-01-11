tab = [29, 10, 23, 16, 8, 24, 22, 20 ,28, 2, 9, 18, 14, 25, 13, 6, 15, 4, 5, 30, 26, 3, 12]
search = 5

def sort(array):
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binSearchRek(tab, s, p, q):
    n = (p + q) // 2

    if tab[n] == s:
        return 1
    if p == q:
        return 0
    if s < tab[n]:
        return binSearchRek(tab, s, p, n - 1)
    else:
        return binSearchRek(tab, s, n + 1, q)

print(binSearchRek(sort(tab), search, 0, len(tab) - 1))