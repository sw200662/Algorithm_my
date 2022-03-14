n = 5
edges = [[0,1],[0,2],[1,3],[1,4]]

tree = [[] for _ in range(n)]

for i in edges:
    tree[i[0]].append(i[1])

answer = 0
for x in range(n):
    for y in range(n):
        if x != y:
            for z in range(n):
                if x !=y and y !=z and x != z:
                    point = [x,y,z]
