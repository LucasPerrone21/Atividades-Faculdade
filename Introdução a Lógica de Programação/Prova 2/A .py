N_Jedi , XPGanho , XPmin = map(int,input().split())
for Z in range(N_Jedi):
    XP_Jedi , N_Missoes = map(int, input().split())
    if XP_Jedi < XPmin:
        print(XP_Jedi, N_Missoes)
    else:
        print( XP_Jedi + XPGanho , N_Missoes + 1)