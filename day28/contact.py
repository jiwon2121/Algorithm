import sys
sys.stdin = open('./input1.txt')
from collections import deque

T = 10
for tc in range(1, T + 1):
    N, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    adj = [set() for _ in range(101)]
    called = [0 for _ in range(101)]
    for i in range(0, N, 2):
        adj[from_to[i]].add(from_to[i + 1])

    que = deque([start])
    called[start] = 1
    max_cnt = 0
    max_num = 0
    while que:
        curr = que.popleft()
        if called[curr] > max_cnt:
            max_cnt = called[curr]
            max_num = curr
        elif called[curr] == max_cnt:
            max_num = max(max_num, curr)

        for nxt in adj[curr]:
            if not called[nxt]:
                que.append(nxt)
                called[nxt] = called[curr] + 1

    print(f'#{tc}', max_num)