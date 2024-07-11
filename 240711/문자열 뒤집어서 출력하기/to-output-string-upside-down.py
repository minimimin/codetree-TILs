from collections import deque

words = deque()
for _ in range(4):
    words.append(input())
for sunseo in range(4):
    print(words.pop()[::-1])