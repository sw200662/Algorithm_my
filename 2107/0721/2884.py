A, B = map(int,input().split())

if B < 45:
    B = B + 60 - 45
    A = A - 1
    if A < 0:
        A = A  + 24
else:
    B = B - 45

print(A,B)