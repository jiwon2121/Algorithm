import sys
sys.stdin = open('./input.txt')

from heapq import heappop, heappush

def dijk(start):
    dist = [inf for _ in range(N+1)]
    dist[start] = 0
    hp = []
    heappush(hp, (0, start))

    while hp:
        value, curr = heappop(hp)
        for weight, nxt in adj[curr]:
            weight += value
            if dist[nxt] > weight:
                dist[nxt] = weight
                heappush(hp, (weight, nxt))

    if start == X:
        return dist

    return dist[X]


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    inf = 1e9
    adj = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x].append((c, y))

    start_x = dijk(X)

    result = 0
    for i in range(1, N+1):
        if i == X:
            continue
        result = max(result, start_x[i] + dijk(i))

    print(f'#{tc}', result)
