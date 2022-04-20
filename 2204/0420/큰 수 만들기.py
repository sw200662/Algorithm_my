number = "1231234"
k = 3

def solution(number, k):
    answer = ''
    a = []
    for i in number:
        while a and a[-1] < i and k>0:
            k-=1
            a.pop()
        a.append(i)
    a = "".join(a[:len(a)-k])
    return a

solution(number, k)