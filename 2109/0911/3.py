def solution(id_list, report, k):
    report = list(set(report))
    a = []
    b = []
    c = []
    answer = [0] * len(id_list)
    for i in report:
        a += i.split()
    for q in range(len(a)):
        if q % 2 == 0:
            b.append(a[q])
        else:
            c.append(a[q])
            
    check_list = [0] * len(id_list)
    
    for z in range(len(c)):
        if c[z] in id_list:
            check_list[id_list.index(c[z])] +=1
                
    for r in range(len(check_list)):
        if check_list[r] >= k:
            for f in range(len(c)):
                if id_list[r] == c[f]:
                    answer[id_list.index(b[f])] +=1

    return answer