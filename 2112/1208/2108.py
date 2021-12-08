import sys
from collections import Counter

sys.stdin = open('input.txt')

N = int(input())
number = []
for _ in range(N):
    number.append(int(sys.stdin.readline()))
number.sort()
cnt = Counter(number).most_common(2)
print(round(sum(number)/len(number)))
print(number[len(number)//2])
# for i in find_number:
#     cnt_number.append([number.count(i),i])
# cnt_number = sorted(cnt_number, key=lambda x: (x[0], -x[1]))
# if cnt_number[-1][0] == cnt_number[-2][0]:
#     print(cnt_number[-2][1])
# else:
#     print(cnt_number[-1][1])
if len(number) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(number)-min(number))
