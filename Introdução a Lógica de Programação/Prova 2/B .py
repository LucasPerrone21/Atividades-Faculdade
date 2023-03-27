Valores = list(map(float, input().split()))
Valores = sum(Valores[1:])
if Valores > 940.00:
    print('Saldo insuficiente. Coitadinho do Seu Toinho.')
else:
    Valores = 940 - Valores
    print('R$', "{:.2f}".format(Valores))