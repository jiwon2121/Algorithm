import sys
sys.stdin = open('./5247_input.txt')
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    que = deque([N])
    used = [0 for _ in range(1000001)]
    used[N] = 1

    while True:
        num = que.popleft()

        if num + 1 == M or num * 2 == M or num - 1 == M or num - 10 == M:
            cnt = used[num]
            break
        if num + 1 <= 1000000 and not used[num + 1]:
            que.append(num + 1)
            used[num + 1] = used[num] + 1
        if num * 2 <= 1000000 and not used[num * 2]:
            que.append(num * 2)
            used[num * 2] = used[num] + 1
        if num - 1 >= 1 and not used[num - 1]:
            que.append(num - 1)
            used[num - 1] = used[num] + 1
        if num - 10 >= 1 and not used[num - 10]:
            que.append(num - 10)
            used[num - 10] = used[num] + 1

    print(f'#{tc}', cnt)
    # print(used)
