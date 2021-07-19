SCORE = int(input())

if SCORE >= 90:
    print('A')
elif 89 >= SCORE >= 80:
    print('B')
elif 79 >= SCORE >= 70:
    print('C')
elif 69 >= SCORE >= 60:
    print('D')
else:
    print('F')