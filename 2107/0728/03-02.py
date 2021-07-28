def sum_of_repeat_number(numbers):
    ans = []
    for Number in numbers:
        if numbers.count(Number) == 1:
            
            ans.append(Number)
    return(sum(ans))

print(sum_of_repeat_number([4, 4, 7, 8, 10]))

