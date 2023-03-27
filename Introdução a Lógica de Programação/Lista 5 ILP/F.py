M = []
for U in range (10):
    S = input()
    Aux = []
    for c in range (19):
        if (S[c] != ' ' ):
            Aux.append(S[c])
    M.append(Aux)
for c in range (10):
    for j in range(10):
        if (M[c+1][j] == '*') or (M[c-1][j] == '*') or (M[c][j+1] == '*') or (M[c][j-1] == '*'):
            M[c][j] = 'p'
print(M)