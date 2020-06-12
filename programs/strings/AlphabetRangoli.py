
def print_rangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

def print_rangoli_solution2(n):
    import string
    alpha = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))


n = int(input())
print_rangoli(n)
print_rangoli_solution2(n)