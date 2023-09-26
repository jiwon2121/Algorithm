from heapq import heappop, heappush

problem = 0
inf = 1e9
delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]

while True:
    N = int(input())

    if N == 0:
        break

    problem += 1
    array = [list(map(int, input().split())) for _ in range(N)]
    dist = [[inf for _ in range(N)] for _ in range(N)]
    dist[0][0] = array[0][0]
    que = list()
    que.append((array[0][0], [0, 0]))

    while que:
        value, loc = heappop(que)

        for d1, d2 in delta:
            ni = loc[0] + d1
            nj = loc[1] + d2

            if 0 <= ni < N and 0 <= nj < N:
                next_v = value + array[ni][nj]

                if next_v < dist[ni][nj]:
                    heappush(que, (next_v, [ni, nj]))
                    dist[ni][nj] = next_v

    print(f'Problem {problem}: {dist[N-1][N-1]}')