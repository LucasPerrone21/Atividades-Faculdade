N_de_Caixas = int(input())
N_de_Esmeraldas = []
N_de_Esmeraldas.extend(input().split())
N_Correto = str(input())
if N_Correto in N_de_Esmeraldas:
    print(N_Correto)
else:
    print(-1)