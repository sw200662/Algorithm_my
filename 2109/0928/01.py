import sys

sys.stdin = open('input.txt')


# def check_connect(a,b):
#     global ans
#     if len(a) == 1:
#         pass
#     else:
#         for i in a:
#             check = 0
#             temp_list = list_dosi[i-1][1:]
#             for k in temp_list:
#                 if k in sungo1:
#                     check += 1
#             if check == 0:
#                 return
#
#     if len(b) == 1:
#         pass
#     else:
#         for i in b:
#             check = 0
#             temp_list = list_dosi[i-1][1:]
#             for k in temp_list:
#                 if k in sungo2:
#                     check += 1
#             if check == 0:
#                 return
#     dosi1 = 0
#     dosi2 = 0
#     for c in a:
#         dosi1 += People[c-1]
#     for d in b:
#         dosi2 += People[d-1]
#     temp_ans = abs(dosi1-dosi2)
#     if temp_ans < ans:
#         ans = temp_ans
#         print(sungo1)
#         print(sungo2)
#         print(ans)
def sum_people(a,b):
    global ans
    dosi1 = 0
    dosi2 = 0
    for c in a:
        dosi1 += People[c-1]
    for d in b:
        dosi2 += People[d-1]
    temp_ans = abs(dosi1-dosi2)
    if temp_ans < ans:
        ans = temp_ans

def bfs(a,b):
    global check_templist
    if a not in check_templist:
        if a in b:
            check_templist.append(a)
            temp_dosi = list_dosi[a-1]
            for k in range(1,len(temp_dosi)):
                bfs(temp_dosi[k],b)


N = int(input())
People = list(map(int, input().split()))
list_dosi = [list(map(int, input().split())) for _ in range(N)]
sungo = []

ans = 500
for i in range(1, N + 1):
    sungo.append(i)
for i in range(1 << N):
    check_templist = []
    sungo1 = []
    sungo2 = sungo[:]
    for j in range(N):
        if i & (1 << j):
            k = sungo[j]
            sungo1.append(k)
            sungo2.remove(k)
    if len(sungo1) == 0 or len(sungo2) == 0:
        pass
    else:
        bfs(sungo1[0],sungo1)
        check_templist.sort()
        if sungo1 == check_templist:
            check_templist = []
            bfs(sungo2[0],sungo2)
            check_templist.sort()
            if sungo2 == check_templist:
                sum_people(sungo1,sungo2)

if ans == 500:
    print(-1)
else:
    print(ans)
