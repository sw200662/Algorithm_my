logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
find = ["team_name ","application_name ","error_level ","message "]

answer = 0
for i in logs:
    if len(i) > 100:
        continue
    check_point = []
    flag = 0
    check = 0
    for a in range(len(i)):
        if i[a] == ':':
            if check == 0:
                if i[:a] not in find:
                    flag = 1
                    break
            if i[a-len(find[check]):a] not in find:
                flag = 1
                break
            if check == 0:
                check_point.append(a+1)
            else:
                check_point.append(a-len(find[check])-1)
                check_point.append(a + 1)
            check += 1
    if check != 4 or flag == 1:
        continue
    check_point.append(len(i))
    for b in range(len(check_point)//2):
        c,d = check_point[b*2], check_point[b*2+1]
        e = i[c+1:d]
        upper = sum(f.isupper() for f in e)
        lower = sum(f.islower() for f in e)
        if upper + lower != len(e):
            flag = 1
            break
    if flag == 1:
        continue
    answer += 1
