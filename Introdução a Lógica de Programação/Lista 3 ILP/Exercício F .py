a, b = map(int,input().split())
num = 0
for c in range (a, b + 1):
    cont = 0
    for j in range (1, c + 1):
        if (c % j == 0):
            cont += 1
    if cont <= 2:
        num += 1
print(num)