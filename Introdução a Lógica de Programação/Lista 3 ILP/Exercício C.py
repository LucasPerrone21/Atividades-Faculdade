Pi = str
Sat = int
while (Pi != '#'):
    Pi, Sat = input().split()
    Sat = int(Sat)
    if 0 < Sat < 90:
        print(Pi, 'Internar')
    if Sat >= 90:
        print(Pi, 'Alta')
        