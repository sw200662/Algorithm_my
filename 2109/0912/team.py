import math
print(180 / math.pi * math.atan(-2/2))
print(180 / math.pi * math.atan(2/2))
print(180 / math.pi * math.atan(2/-2))
print(180 / math.pi * math.atan(-2/-2))
# atan2(y,x) # 목표구 - 수구

print(180 / math.pi * math.atan2(2,2))  # 1사분면
print(180 / math.pi * math.atan2(2,-2)) # 2사분면, 90 -> 360(450 - 90), 180 -> 270(450-180)
print(180 / math.pi * math.atan2(-2, -2))    #3사분면 -90 -> 180(90 - (-90)), -180 -> 270 (90 - (-180))
print(180 / math.pi * math.atan2(-2,2)) # 4사분면 0 -> 90, (90 - 0) -> 180 (90 - (-90))

print(90 - 180 / math.pi * math.atan2(2,2))  # 1사분면
print(450 - 180 / math.pi * math.atan2(2,-2)) # 2사분면, 90 -> 360(450 - 90), 180 -> 270(450-180)
print(90 - 180 / math.pi * math.atan2(-2, -2))    #3사분면 -90 -> 180(90 - (-90)), -180 -> 270 (90 - (-180))
print(90 - 180 / math.pi * math.atan2(-2,2)) # 4사분면 0 -> 90, (90 - 0) -> 180 (90 - (-90))

# 결론은 아래로 통일
# print(90 - 180 / math.pi * math.atan2(y,x))

# 홀 위치 정하기
# HOLE[0] = [0,0]
# HOLE[1] = [127,0]
# HOLE[2] = [254,0]
# HOLE[3] = [0,127]
# HOLE[4] = [127,127]
# HOLE[5] = [254,127]
"""
x 좌표의 가운데(127)를 기준으로 왼쪽에 존재하면 0, 1, 3, 4
x 좌표의 가운데(127)를 기준으로 오른쪽에 존재하면 1, 2, 4, 5
목적구를 기준으로 수구가 1사분면에 위치하면 3사분면 방향
목적구를 기준으로 수구가 2사분면에 위치하면 4사분면 방향
목적구를 기준으로 수구가 3사분면에 위치하면 1사분면 방향
목적구를 기준으로 수구가 4사분면에 위치하면 2사분면 방향
"""

TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [ [0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127] ]
r = 5.73 / 2
white = balls[0]
arrival = HOLES[0]
# gameball[0] => 흰색 공
# gameball[1] => 목적 공
# 목적구 정하기
if player == 1: # 선공
    ball_list = [balls[1], balls[3], balls[5]]

else: # 후공
    ball_list = [balls[2], balls[4], balls[5]]

real_min = 300          # 홀과 목적구의 최소 값
purposes = ball_list[0] # 최종 목적구
arrivals = HOLES[0]     # 최종 홀
flag = 0
for j in range(3):
    if (ball_list[j][0] == 0) and (ball_list[j][1] == 0): # 만약 이미 들어간 홀이면
        flag += 1
        continue

    if (j == 2) and (flag != 2): # 만약 둘 다 없으면 검은공을 목적구로 설정
        continue

    purpose = ball_list[j]  # 현재 목적구
    # 홀 위치 정하기
    if purpose[j][0] <= 127:
        holes_list = [HOLES[0], HOLES[1], HOLES[3], HOLES[4]]
    else:
        holes_list = [HOLES[1], HOLES[2], HOLES[4], HOLES[5]]

    min = 300 # (254^2 + 127^2)^(0.5) = 284
    for i in range(4):
        if ((holes_list[i][0] - purpose[j][0])**2 + (holes_list[i][1] - purpose[j][1])**2)**(0.5) < min:
            min = ((holes_list[i][0] - purpose[j][0])**2 + (holes_list[i][1] - purpose[j][1])**2)**(0.5)
            arrival = holes_list[i] # 홀의 위치

    if min < real_min:  # 홀과 가장 가까운 목적구 찾기
        real_min = min      # 홀과 목적구의 최소 거리
        purposes = purpose  # 최종 목적구를 현재 목적구로 정함
        arrivals = arrival  # 최종 홀을 현재 목적구랑 가까운 홀로 정함

# 홀 위치 - 목적구 위치 대각선 길이
b = ((arrivals[0] - purposes[0])**2 + (arrivals[1] - purposes[1])**2)**(0.5)

# 홀과 목적구의 y 값의 차이 / 대각선의 길이에 arccos 적용으로 세타 구하기
theta = math.acos(abs(arrivals[1] - purposes[1]) / b)  # 라디안
print(180 / math.pi * theta)    # 디그리

# (대각선 길이 + 2r)에  cos  세타를 곱하면 옮길 목적구 까지의 y 수정값 알 수 있음
# cos 세타 적용해서 나온 y값을 목적구에서 빼거나 더해줌
new_y = (b + 2 * r) * math.cos(theta)

# 그 다음은 sin을 이용해서 x 수정값 알 수 있음
# sin세타 적용해서 나온 x값을 목적구에서 더해거나 빼줌
new_x =  (b + 2 * r) * math.sin(theta)

purposes = [new_x, new_y]

angle = (90 - 180 / math.pi * math.atan2(new_y,new_x))
power = 50 # 홀까지 가는데 최소 힘, 너무 쎄면 공이 튕겨 나올지도


if arrivals == HOLES[2]:
    new_x = 254 - new_x
elif arrivals == HOLES[5]:
    new_x = 254 - new_x
    new_y = 127 - new_y
elif arrivals == HOLES[3]:
    new_y = 127 - new_y
elif arrivals == HOLES[4]:
    if purposes[0] <= 127:
        new_x = 127 - new_x
        new_y = 127 - new_y
    else:
        new_x = 127 + new_x
        new_y = 127 - new_y