T = int(input())

for Test in range(T):
    Value = list(map(int,input().split()))
    P = Value[0]
    Q = Value[1]
    R = Value[2]
    S = Value[3]
    W = Value[4]
    A_bill = 0
    B_bill = 0
    
    A_bill = P * W
    if W < R:
        B_bill = Q
    else:
        B_bill = Q + S*(W - R)
    if A_bill > B_bill:
        print(f'#{Test+1} {B_bill}')
    else:
        print(f'#{Test+1} {A_bill}')