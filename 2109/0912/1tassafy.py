import math

def hole_distance(ball):
    first = 1
    second = 2
    if first:
        # 우선 1,3번공의 위치 확인 > 그다음 먼저 넣고 생각
        # 8번은 가운데 고정이고 1,3둘중 하나는 맨뒤를 제외한 한곳에 배정될테니 우선 이것을 넣는방법에 대해 고려해보자.
        pass
    else:
        # 공의 위치에 따라 홀을 먼저 정한다 > 여기서 2,4번중 무엇을 먼저 넣을지 고민을 해야한다
        # for > 2,4 번
        if 0 < balls[2][0] <= 127:
            find_holes = [HOLES[0],HOLES[1],HOLES[3],HOLES[4]]
        else:
            find_holes = [HOLES[1],HOLES[2],HOLES[4],HOLES[5]]

        
def find_distance(n): # n은 우리가 찾을 볼의 숫자
    pass




balls = []

x=3
y=3

angle = 90-180/math.pi * math.atan2(x,y)
x = 3
y = 5

z = math.acos(x/y)
c = y * math.sin(z)
print(c)

TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [ [0,0], [127,0], [254,0], [0,127], [127,127], [254,127]]
r = 5.73/2
print(HOLES)