num_teams = 2
remote_tasks = ["design"]
office_tasks = ["building", "supervise"]
employees = ["2 design", "1 supervise building design", "1 design", "2 design"]
team = []
person = []
first_person = dict()
first_team = []
for i in range(len(employees)):
    a = employees[i].split()
    if a[0] not in first_team:
        first_team.append(a[0])
        first_person[a[0]] = i+1
    for b in range(1,len(a)):
        if a[b] in office_tasks:
            team.append(int(a[0]))
            person.append(i+1)
            break

all_team = list(range(1,num_teams+1))
all_person = list(range(1,len(employees)+1))
for c in all_team:

    if c not in team:
        person.append(first_person[str(c)])

answer = [i for i in all_person if i not in person]

print(answer)
