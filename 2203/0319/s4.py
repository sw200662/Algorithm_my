from collections import deque


def solution(arr, process):
    def readgo():
        global time
        recent_time = time

        while len(read) != 0:
            a = read.popleft()
            t1, t2, t3, t4 = a.split()
            t1 = int(t1)
            t2 = int(t2)
            t3 = int(t3)
            t4 = int(t4)
            if recent_time > t1:
                t1 = recent_time
            if t1 + t2 > time:
                time = t1 + t2
            ans.append(arr[t3:t4 + 1])
            for i in range(t1, t1 + t2 + 1):
                visit[i] = 1

    def writego():
        global time
        recent_time = time

        while len(write) != 0:
            a = write.popleft()
            t1, t2, t3, t4, t5 = a.split()
            t1 = int(t1)
            t2 = int(t2)
            t3 = int(t3)
            t4 = int(t4)
            t5 = int(t5)
            if recent_time > t1:
                t1 = recent_time
            if t1 + t2 > time:
                time = t1 + t2
            for i in range(t1, t1 + t2 + 1):
                visit[i] = 1
            for b in range(t3, t4 + 1):
                arr[b] = str(t5)
            recent_time = time

    global time
    time = 0
    visit = [0] * 99999
    read = deque()
    write = deque()
    ans = []
    anstime = 0
    for i in process:
        if i[0] == "r":
            a1, a2, a3, a4, a5 = i.split()
        else:
            a1, a2, a3, a4, a5, a6 = i.split()
        if i[0] == "r" and time < int(a2):
            if len(write) == 0:
                read.append(i[5:])
            else:
                writego()
                read.append(i[5:])
        elif i[0] == "r" and time >= int(a2):
            writego()
            read.append(i[5:])
        elif i[0] == "w" and time > int(a2):
            write.append(i[6:])
        else:
            if len(write) == 0 and time == int(a2):
                write.append(i[6:])
                writego()
            elif len(write) == 0 and time != int(a2):
                readgo()
                write.append(i[6:])
            else:
                writego()
                write.append(i[6:])
    readgo()
    for i in range(len(visit)):
        if visit[i] == 1:
            anstime += 1
        if i > 1 and visit[i] == 0 and visit[i - 1] == 1:
            anstime -= 1

    ans2 = []

    for i in ans:
        temp = ''
        for a in i:
            temp += a
        ans2.append(temp)
    ans2.append(str(anstime))
    return (ans2)

