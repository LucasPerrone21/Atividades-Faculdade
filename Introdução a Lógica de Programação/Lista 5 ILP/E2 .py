N , Tp = map(int,input().split())
Matriz = []
Contador = 0
for C in range (N):
    C = list(map(int, input().split()))
    Matriz.append(C)
for C in range (Tp):
    X, Y = map(int, input().split())
    for C in range (X, -1, -1):
        if Matriz[C][Y] == 1:
            Contador += 1
            Matriz[C][Y] = 0
            break
print(Contador)