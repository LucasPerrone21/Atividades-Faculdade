a =  int(input())
N_Homens=0
N_Mulheres=0
for i in range (a):
    v = int(input())
    total = N_Homens + N_Mulheres
    if v == 1:
        N_Homens = N_Homens + 1
    if v == 2:
        N_Mulheres = N_Mulheres + 1
print(N_Homens)
print(N_Mulheres)