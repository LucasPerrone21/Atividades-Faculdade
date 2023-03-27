Quant_N = int(input())
Pares = []
Impares = []
Numeros = list(map(int, input().split()))
for N in range (Quant_N):
    if int(Numeros[N]) % 2 == 0:
        Pares.append(Numeros[N])
    else:
        Impares.append(Numeros[N])
print(*Pares,sep=' ')
print(*Impares,sep=' ')