import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())
word = str(input().rstrip())
find_word = ''
answer = 0
for a in range(N*2+1):
    if a%2 == 0:
        find_word = find_word + 'I'
    else:
        find_word = find_word + 'O'
for i in range(M):
    if word[i] == 'I':
        if word[i:i+len(find_word)] == find_word:
            answer += 1
print(answer)