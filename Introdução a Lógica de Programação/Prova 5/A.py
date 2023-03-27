A = int(input())
B= list(map(int, input().split()))
for inicio in range(A-1,-1,-1):
    i=inicio
    while i>=1 and B[i] < B[i-1]:
          B[i],B[i-1]=B[i-1],B[i]
          i-=1
print(*reversed(B),sep=' ')