Doce = int(input())
if(Doce / 3 == Doce // 3):
    print("Chapeuzinho Vermelho", Doce // 3 , "\nVovozinha", Doce // 3, "\nLobo Mau" , Doce // 3)
elif(Doce / 3 - Doce // 3 < 0.66666 ):
    print("Chapeuzinho Vermelho", Doce // 3 + 1 , "\nVovozinha", Doce // 3 , "\nLobo Mau" , Doce // 3)
elif(Doce / 3 - Doce // 3 > 0.666666):
    print("Chapeuzinho Vermelho", Doce // 3 + 1 , "\nVovozinha", Doce // 3 + 1, "\nLobo Mau" , Doce // 3)