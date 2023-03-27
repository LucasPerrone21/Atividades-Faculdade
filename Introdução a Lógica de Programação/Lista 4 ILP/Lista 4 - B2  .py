D = int(input())
PontoA = list(map(int, input().split()))
PontoB = list(map(int, input().split()))
PontoDesejado = list(map(int, input().split()))
PontoObtido = []
for i in range (D):
    NC = PontoA[i] + PontoB[i]
    PontoObtido.append(NC)
if PontoObtido == PontoDesejado:
    print('OK')
else:
    print('NOPE :(')