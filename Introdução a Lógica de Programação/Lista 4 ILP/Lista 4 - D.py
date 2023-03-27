Pisadas = []
NumSapos , NumPedras = map(int, input().split())
for Pedras in range (NumPedras):
    Pisadas.append(0)
for salto in range (NumSapos):
    Sapinho = int(input())
    for j in range (0, NumPedras, Sapinho):
        Pisadas[j] = 1
print(*Pisadas, sep= ' ')