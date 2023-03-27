a, b, c = input().split()
K = int(a) + int(b) + int(c)
X = (100 * K) / 110
if(0<=X<50):
    print('Seu pokemon nao fara progresso em batalhas')
if(50<=X<66):
    print('Seu pokemon esta acima da media')
if(66<=X<79):
    print('Seu pokemon certamente me chamou atencao')
if(100>=X>79):
    print('Seu pokemon e uma maravilha')
if(X>100):
    print('Hum, parece que houve um erro')