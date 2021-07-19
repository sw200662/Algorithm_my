YEAR = int(input())

if YEAR % 4 == 0 and YEAR % 100 != 0:
    print('1')
elif YEAR % 400 == 0:
    print('1')
else:
    print('0')