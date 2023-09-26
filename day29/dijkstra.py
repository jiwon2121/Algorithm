import sys
sys.stdin = open('./5251_input.txt')

from heapq import heappop, heappush


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    inf = 1e9
    dist = [inf for _ in range(N + 1)]
    heap = []

    dist[0] = 0
    heappush(heap, (0, 0))
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])

    while heap:
        value, curr = heappop(heap)

        for nxt, weight in adj[curr]:
            d = value + weight
            if dist[nxt] > d:
                dist[nxt] = d
                heappush(heap, (d, nxt))

    print(f'#{tc} {dist[-1]}')