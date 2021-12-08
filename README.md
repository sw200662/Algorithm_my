# TIL(Today I Leared)

 	1. 주로 백준의 알고리즘 푼것을 올릴 예정입니다.

## 01. 비트연산자

& 비트 단위로 AND

| 비트 단위로 OR

<< 비트 열을 왼쪽으로 밈

1 << n : 원소가 n개읠 경우 모둔 부분집합의 수

1 & (1<<j) : i의 j번쨰 비트가 1인지 아닌지를 리턴

```python
arr = [3,6,7,1,5,4]

n = len(arr)

for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            print(arr[j], end=", ")
    print()
print()


```

## 02. Sort와 Sorted

Sort는 > 리스트에서만 사용하고 원본 리스트도 변환  > X.sort()

Sorted > 모두 사용가능하며 변환된값을 리턴해줌 > Y = sorted(X)

Sorted는 다양하게 활용가능 ex> Y = sorted(X, reverser = True)

​														Y = sorted(X.items()

```python
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list) # 2, 3, 4, 5, 6, 8
_list.sort()
print(_list) # 2, 3, 4, 5, 6, 8

_set = {65, 12, 15, 156, 31, 54, 94, 82, 31}
_set.sort() # Error!!!!
print(sorted(_set)) # 12, 15, 31, 54, 65, 82, 94, 156

#내림차순
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list, reversed = True) # 8, 6, 5, 4, 3, 2

#튜플의 리스트를 정렬하고 싶은데, 첫번째 값으로 오름차순 정렬을 하는데 값이 같으면 두번째 값으로 내림차순 정렬하고 싶어...
_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: dt[1]) # (8, 2), (1, 3), (2, 5), (4, 7)

_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: (dt[1], -dt[0])) # (8, 2), (1, 3), (2, 5), (4, 7)

_list = ["CHicken", "hamburger", "Sushi", "chocolate"]

print(sorted(_list)) # ['CHicken', 'Sushi', 'chocolate', 'hamburger']
print(sorted(_list, key = lambda dt: dt.lower())) # ['CHicken', 'chocolate', 'hamburger', 'Sushi']
```



## 03. STACK

스택은 LIFO > Last in First out(나중에 넣은게 먼저 나옴)

## 04 Queue

큐 는 FIFO > First in First out(먼저 넣은게 먼저 나옴)

리스트는 큐로 사용하지 말것(스택의 경우는 뒤에걸 지워서 없애고 끝이지만, 큐는 앞에걸 지우고 뒤의것들을 떙겨오는 구조)

Deque 활용

```python
from collections import deque

a_list = deque('asd')
=> ['a','s','d']
# 2. 뒤에 k를 추가
a_list.append(k)
=> ['a','s','d','k']

# 2.-1앞에 h를 추가
a_list.appendleft(h)
=> ['h','a','s','d']

# 맨 뒤에 pop
a_list.pop()
['a','s']

# 맨 앞에 pop
a_list.popleft()
['s','d']

a_list = deque('asd')
=> ['a','s','d']

#? 잘 모르겟음
a_list.extend('7')  <--그냥 숫자 7 넣으면 typeError
=> ['a','s','d','7']

b_list = [99]
a_list.extendleft(b_list) <-- 리스트를 합치면 int 값이 들어간다.
=> [99,'a','s','d']

print(a_list[0] + 1)
=> 100

#a_list.insert(2,'k') : 2번 index에 'k' 삽입
=> ['a','s,'k','d']

a_list.remove('s') 
=> ['a','d']
    
a_list = deque('asd')
=> ['a','s','d']

a_list.rotate(1)
=> ['d','a','s']

a_list.rotate(-1)
=> ['s','d','a']
```



## 05. 편한 방법들

```python
_list = [1, 2, 3, 4, 5]
first_index, *rest, last_index = _list
print(rest) # 2 3 4

_list = [1, 2, 3, 4, 5]
print(*_list) # 1 2 3 4 5

# 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 바꿔서 저장합시다.
_list = [i if i <= 15 else 15 for i in tmp]

# 두 개의 리스트를 합치되, 가능한 모든 조합을 저장하는 리스트를 만들어봅시다.
x = [i for i in range(5)]
y = [i for i in range(5)]
_list = [(i, j) for i in x, for j in y]

#dict
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price)) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}


#defaultdict
from collections import defaultdict

movie_review = [('Train to Busan', 4), ('Clementine', 5), ('Parasite', 4.5), ('Train to Busan', 4.2), ('Train to Busan', 4.5), ('Clementine', 5)]

index = defaultdict(list)

for review in movie_review:
    index[review[0]].append(review[1]) # {'Train to Busan': [4, 4.2, 4.5], 'Clementine': [5, 5], 'Parasite': [4.5]}
    

#dict 언패킹 여러방법
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(*_dict.keys()) # apple grape orange banana
print(*_dict.values()) # 3200 15200 9800 5000
print(*_dict.items()) # ('apple', 3200) ('grape', 15200) ('orange', 9800) ('banana', 5000)
```

### 06. 문자열

`combination`은 모든 조합을 출력합니다. 즉, 중복이 없고, 순서를 구분하지 않습니다. `permutation`은 순열입니다. 중복은 없지만, 순서를 구분합니다.

`combination_with_replacement`는 중복이 가능한 조합입니다. 그래서 combination과 구분하여 11, 22, 33, 44가 새로 들어오죠. 마지막으로 `product`는 모든 가능한 경우의 수를 출력합니다. (**Cartesian Product**라고 합니다!)

```python
print('     asdasd     '.strip()) # asdasd
print('===chicken==='.strip('=')) # chicken

#문자열 뒤집기
string = 'I am Hungry...'
print(string[::-1])
print("".join(reversed(string)))

#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하시오
import itertools
_list = [1, 2, 3, 4]
iter = itertools.combinations(_list, 2) # 12 13 14 23 24 34

iter = itertools.permutations(_list, 2) # 12 13 14 21 23 24 31 32 34 41 42 43

iter = itertools.combinations_with_replacement(_list, 2) # 11 12 13 14 22 23 24 33 34 44

iter = itertools.product(_list, repeat=2) # 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44

_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(', '.join(_list))

#Enumerate
_list = [a, b, c, d, e, f, g]
for idx, val in enumerate(_list):
    print(idx, val)
    
#counter 
from collections import Counter
Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

from collections import Counter
Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter('hello world').most_common(2) # [('l', 3), ('o', 2)]
```

## 07. BFS DFS

DFS > 깊이 우선 탐색 ()

BFS > 너비 우선 탐색(인접 정점 모두 방문) > 큐 사용

## 08. KMP, 보이어 - 무어, 

KMP 앞에서 부터 패턴 찾으면서, 패턴이 존재하면 그만큼 점프해서 찾음 > 좋지 않아서 많이x

보이어 - 무어 끝글자부터 확인, 그리고 틀리다면 단어를 확인해서 안에 존재한다면 거기까지 점프, 만약 없다면 전체 점프해버림 > 많이 활용

