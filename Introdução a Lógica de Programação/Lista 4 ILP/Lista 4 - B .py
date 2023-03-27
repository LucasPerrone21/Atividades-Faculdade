from xml.dom.minidom import Element


dimensao = int(input())
pontoA = []
pontoA.extend(input().split())
NpontoA = [int(str) for str in pontoA]
pontoB = []
pontoB.extend(input().split())
NpontoB = [int(str) for str in pontoB]
PontoFinal = []
PontoFinal.extend(input().split())
NPontoFinal = [int(str) for str in PontoFinal]
PontoProvavel = [ElePA + ElePB for ElePA, ElePB in zip(NpontoA, NpontoB)]
if NPontoFinal == PontoProvavel:
    print('OK')
else:
    print("NOPE :(")