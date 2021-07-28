def collatz(num):
    count = 0
    while count < 500 and num != 1:
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
    if count == 500:
        return - 1
    return count

print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))