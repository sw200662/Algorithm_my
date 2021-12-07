# TIL(Today I Leared)

 	1. 주로 알고리즘 푼것을 올릴 예정입니다.

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

​														Y = sorted(X.items())

​														

## 03. STACK

스택은 LIFO > Last in First out(나중에 넣은게 먼저 나옴)

## 04 Queue

큐 는 FIFO > First in First out(먼저 넣은게 먼저 나옴)
