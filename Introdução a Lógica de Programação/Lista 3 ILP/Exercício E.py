T = int(input())
while True:
   B = int(input())
   if B > T:
       fds = input()
       c = "ALARME"
       break
   if B < T:
       c = "O Havai pode dormir tranquilo"
       if B == 0:
           break
       else:
           continue
print(c)