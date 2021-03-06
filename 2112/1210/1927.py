import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

heap = [0] * N
end = 0

for _ in range(N):
    a = int(input())
    i = 1
    if a == 0:
        if heap[1] == 0:
            print(0)
        else:
            print(heap[1])
            heap[1],heap[end] = heap[end], heap[1]
            end -= 1

            idx = 1
            child = 2
            while end >= child:
                if child < end and heap[child] < heap[idx]:
                    heap[child], heap[idx] = heap[idx], heap[child]


    else:
        end += 1
        heap[end] = a
        b = end
        if end != 1:
            while True:
                if heap[b] < heap[b//2]:
                    heap[b],heap[b // 2] = heap[b // 2], heap[b]
                    b = b//2
                else:
                    break