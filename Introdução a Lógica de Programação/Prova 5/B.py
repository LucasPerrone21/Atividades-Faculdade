A = int(input())
Matriz = []
valorfinal=0
for c in range (A):
    listaaux = []
    X, Y = input().split()
    Y = int(Y)
    listaaux.append(X)
    listaaux.append(Y)
    Matriz.append(listaaux)
for c in range(int(input())):
    X, Y = input().split()
    Y = int(Y)
    esq = 0
    dir = A - 1
    while esq <= dir:
        g = 0
        meio = (esq + dir) // 2
        if Matriz[meio][0] == X:
            g = Matriz[meio][1]*Y
        elif Matriz[meio][0] > X:
            esq = meio + 1
        else:
            dir = meio - 1
            break
    valorfinal += g
print(valorfinal)