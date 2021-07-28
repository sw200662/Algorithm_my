def my_find(text, alphabet):
    ans = []
    count = 0
    out = 0
    for A in text:
        if A == alphabet:
            ans += [count]
            out += 1
        count += 1

    if out >= 1:
        return ans
    return -1

print(my_find('apple', 'p'))
print(my_find('a', 'p'))