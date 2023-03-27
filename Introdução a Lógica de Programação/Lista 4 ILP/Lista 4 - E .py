NumDeEsferas = int(input())
Comp = []
EsferasAchadas = list(map(int, input().split()))
for j in range (NumDeEsferas):
    if EsferasAchadas[j] == 1:
        MJ = EsferasAchadas[j]
        Comp.append(MJ)
    if EsferasAchadas[j] == 2:
        MJ = EsferasAchadas[j]
        Comp.append(MJ)
    if EsferasAchadas[j] == 3:
        MJ = EsferasAchadas[j]
        Comp.append(MJ)
    if EsferasAchadas[j] == 4:
        MJ = EsferasAchadas[j]
        Comp.append(MJ)
    if EsferasAchadas[j] == 5:
        MJ = EsferasAchadas[j]
        Comp.append(MJ)
    if EsferasAchadas[j] == 6:
        MJ = EsferasAchadas[j]
        Comp.append(MJ)
    if EsferasAchadas[j] == 7:
        MJ = EsferasAchadas[j]
        Comp.append(MJ)
if sorted(Comp) == [1,2,3,4,5,6,7]:
    print(*sorted(Comp), sep=' ')
    print('Saia Shenlong e realize o meu desejo')
else:
    print(*sorted(Comp), sep=' ')
    print('Nao encontramos todas')