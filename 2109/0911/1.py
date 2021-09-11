def solution(id_list, report, k):
    report = list(set(report))
    a = []
    answer = [0] * len(id_list)
    for i in report:
        a += i.split()
        
    check_list = [0] * len(id_list)
    
    for z in range(1,len(a),2):
        if a[z] in id_list:
            check_list[id_list.index(a[z])] +=1
                
    for b in range(len(check_list)):
        if check_list[b] >= k:
            for z in range(1,len(a),2):
                if id_list[b] == a[z]:
                    answer[id_list.index(a[z-1])] +=1

    return answer