def check(n, students):
    Num = list(range(1,n+1))
    student = list((students.split()))
    for i in student:
        Num.remove(int(i))
    return(Num)

print(check(7, '1 3 5'))