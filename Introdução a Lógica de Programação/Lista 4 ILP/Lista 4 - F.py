NumJoga = int(input())
Valores = list(map(int, input().split()))
Lista2 = []
for H in range (0, NumJoga, -1):
    F = Valores[H]
    Lista2.append(F)
print(Lista2)