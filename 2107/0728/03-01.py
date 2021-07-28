def change_rotten_fruit(fruit_bag):
    ans = []
    for Fruit in fruit_bag:
        Fruit = Fruit.replace('rotten','').lower()
        ans.append(Fruit)
    return(ans)

print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))