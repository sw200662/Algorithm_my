def dict_invert(my_dict):
    ans = {}
    for key, values in my_dict.items():
        if values in ans:
            ans[values] += [key]
        else:
            ans[values] = [key]
    return ans

print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))