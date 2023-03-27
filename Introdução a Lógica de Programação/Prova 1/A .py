import math
a = int(input())
b = int(input())
c = int(input())
P1 = math.fabs(b - c)
P2 = math.fabs(a - c)
P3 = math.fabs(a - b)
G1 = b + c
G2 = a + c
G3 = a + b
if((P1 < a < G1) and (P2 < b < G2)and (P3 < c < G3)):
    print("Forma triangulo")
else:
    print("Nao forma triangulo")