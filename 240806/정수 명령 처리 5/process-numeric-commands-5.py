from collections import deque

dyna_arr = deque()

for _ in range(int(input())):
    com = input().split()
    if len(com) == 2:
        if com[0] == 'push_back':
            dyna_arr.append(int(com[1]))
        else:
            print(dyna_arr[int(com[1])-1])
    else:
        if com[0] == 'pop_back':
            dyna_arr.pop()
        else:
            print(len(dyna_arr))