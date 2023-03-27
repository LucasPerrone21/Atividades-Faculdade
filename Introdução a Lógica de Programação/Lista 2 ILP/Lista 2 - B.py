P1_J1, P1_J2 = map(int, input().split())
P2_J1, P2_J2 = map(int, input().split())
P3_J1, P3_J2 = map(int, input().split())

if(P1_J1 + P2_J1 + P3_J1 > P1_J2 + P2_J2 + P3_J2):
    print("Lucas")
elif(P1_J1 + P2_J1 + P3_J1 == P1_J2 + P2_J2 + P3_J2):
    print("Empate")
else:
    print("Pedro")