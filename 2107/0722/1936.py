A = map(int,input().split())
A = list(A)

if A[0] == 1:
    if A[1] == 2:
        print('B')
    else:
        print('A')
elif A[0] == 2:
    if A[1] == 3:
        print('B')
    else:
        print('A')
else:
    if A[1] == 1:
        print('B')
    else:
        print('A')