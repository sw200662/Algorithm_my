T = int(input())
A = 0
for i in range(1,T+1):
    if T % i == 0:
        print(T,end=' ')