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
            heap[end] = 0
            end -= 1


            idx = 1
            child = idx * 2
            while end >= child:
                large = idx
                if child <= end and heap[child] < heap[idx]:
                    idx = child
                if child + 1 <= end and heap[child+1] < heap[idx]:
                    idx = child + 1

                if large != idx:
                    heap[idx], heap[large] = heap[large], heap[idx]
                    large = idx
                    child = large * 2
                else:
                    break
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