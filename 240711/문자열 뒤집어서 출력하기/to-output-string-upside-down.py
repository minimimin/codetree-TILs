from collections import deque

words = deque([input() for _ in range(4)])
for sunseo in range(4):
    print(words.pop()[::-1])