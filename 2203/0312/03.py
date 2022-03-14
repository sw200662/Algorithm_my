import math
x = 51
y = 37

diagonals = [[17,19]]
answer = 0
for i in diagonals:
    a = i[0]
    b = i[1]
    c1 = math.factorial(a+b-1) // (math.factorial(a-1) * math.factorial(b))
    f1 = math.factorial(x+y-a-b+1) // (math.factorial(x-a+1) * math.factorial(y-b))
    c2 = math.factorial(a+b-1) // (math.factorial(a) * math.factorial(b-1))
    f2 = math.factorial(x+y-a-b+1) // (math.factorial(x-a) * math.factorial(y-b+1))
    a1 = c1 * f2
    a2 = c2 * f1
    answer += a1
    answer += a2
print(answer%10000019)

a = math.factorial(35)
b = math.factorial(16) * math.factorial(19)
c1 = a // b
d = math.factorial(x+y-35)
e = math.factorial(x-16) * math.factorial(y-19)
f1 = d // e

a = math.factorial(35)
b = math.factorial(17) * math.factorial(18)
c2 = a // b
d = math.factorial(x+y-35)
e = math.factorial(x-17) * math.factorial(y-18)
f2 = d // e

a1 = c1 * f2
a2 = c2 * f1

answer = a1+a2

