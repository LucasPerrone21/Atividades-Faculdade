A = int(input())
B = list(map(int, input().split()))
Macaco = []
for c in range (0, 1000000):
    if ( c in B):
        Macaco.append(c)
print(*Macaco, sep='')