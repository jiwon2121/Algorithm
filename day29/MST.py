import sys
sys.stdin = open('./5249_input.txt')

from heapq import heappop, heappush


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    heap = []
    res = 0

    heappush(heap, (0, 0))
    visited = 0
    all_visit = (1 << V+1) - 1
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((n2, w))
        adj[n2].append((n1, w))

    while heap:
        if visited == all_visit:
            break

        w, node = heappop(heap)
        if visited & 1 << node:
            continue

        visited = visited | 1 << node
        res += w

        for nxt, weight in adj[node]:
            if not visited & 1 << nxt:
                heappush(heap, (weight, nxt))

    print(f'#{tc} {res}')

