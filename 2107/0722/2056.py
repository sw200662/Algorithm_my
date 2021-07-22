A = int(input())
B = 1

for i in range(A):
    T = str(input())
    YEAR = T[0:4]
    MONTH = T[4:6]
    DAY = T[6:8]

    INT_MONTH = int(MONTH)
    INT_DAY = int(DAY)

    if INT_MONTH == 2:
        if 1 <= INT_DAY <= 28:
            print(f'#{B} {YEAR}/{MONTH}/{DAY}')
        else:
            print(f'#{B} -1')
    elif INT_MONTH == 0:
        print(f'#{B} -1')
    elif INT_MONTH == 4 or INT_MONTH == 6 or INT_MONTH == 9 or INT_MONTH == 11:
        if 1 <= INT_DAY <= 30:
            print(f'#{B} {YEAR}/{MONTH}/{DAY}')
        else:
            print(f'#{B} -1')
    else:
        if 1 <= INT_DAY <= 31:
            print(f'#{B} {YEAR}/{MONTH}/{DAY}')
        else:
            print(f'#{B} -1')
    
    B += 1