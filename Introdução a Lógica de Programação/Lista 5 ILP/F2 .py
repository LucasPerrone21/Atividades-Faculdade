Matriz = []
for C in range (10):
    C = list(map(str, input().split()))
    Matriz.append(C)

for X in range (10):
    for Y in range (10):
        if Matriz[X][Y] == 't':
            if X = 0 and Y = 0:
                # Diagonais
                if Matriz[X+1][Y] == '*':
                    Matriz[X][Y] = 'p'
                    break
                if Matriz[X][Y+1] == '*':
                    Matriz[X][Y] = 'p'
                    break
            if X = 9 and Y = 9:
                if Matriz[X-1][Y] == '*':
                    Matriz[X][Y] = 'p'
                    break
                if Matriz[X][Y-1] == '*':
                    Matriz[X][Y] = 'p'
                    break
            if X = 0 and Y = 9:
                if Matriz[X+1][Y] == '*':
                    Matriz[X][Y] = 'p'
                    break
                if Matriz[X][Y-1] == '*':
                    Matriz[X][Y] = 'p'
                    break
            if X = 9 and Y = 0:
                if Matriz[X-1][Y] == '*':
                    Matriz[X][Y] = 'p'
                    break
                if Matriz[X][Y+1] == '*':
                    Matriz[X][Y] = 'p'
                    break

            if X = 0:
                if Matriz[X][Y+1] == '*':
                    Matriz[X][Y] = 'p'
            if Matriz[X+1][Y] == '*':
                Matriz[X][Y] = 'p'
            if Matriz[X-1][Y] == '*':
                Matriz[X][Y] = 'p'
            if Matriz[X][Y+1] == '*':
                Matriz[X][Y] = 'p'
            if Matriz[X][Y-1] == '*':
                Matriz[X][Y] = 'p'
for c in range (5):
    print(*Matriz[c], sep=' ')