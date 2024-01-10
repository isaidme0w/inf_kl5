# iteracyjnie
def silniaPod(n):
    res = n
    while n >= 3:
        res *= n - 2
        n -= 2
    return res

# rekurencyjnie
def silniaPodRek(n):
    if n <= 1:
        return 1
    else:
        return silniaPodRek(n - 2) * n

a = 11
print("a =", a)
print("Iteracyjnie:", silniaPod(a))
print("Rekurencyjnie:", silniaPodRek(a))