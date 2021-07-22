TEST_CASE = int(input())
b = 1
for i in range(TEST_CASE):
    A,B = map(int,input().split())
    an = A // B
    an2 = A % B
    print(f'#{b} {an} {an2}')
    b +=1