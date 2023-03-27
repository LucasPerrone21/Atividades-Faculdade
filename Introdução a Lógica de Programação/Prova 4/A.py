H, L = map(int,input().split())
Matriz = []
contador = 0
for C in range (H):
    Matriz.append(list(map(int,input().split())))
Tipo = int(input())
for X in range (H):
    for Y in range(L):
        if Matriz[X][Y] == Tipo:
            contador += 1
print('Ash pegou',contador,'pokemon')