import sys
sys.stdin = open('./5250_input.txt')

from heapq import heappop, heappush


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    inf = 1e9
    dist = [[inf for _ in range(N)] for _ in range(N)]
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    heap = []

    dist[0][0] = 0
    heappush(heap, (0, 0, 0)) # w, i, j

    while heap:
        value, i, j = heappop(heap)
        height1 = array[i][j]
        for d1, d2 in delta:
            ni = d1 + i
            nj = d2 + j

            if 0 <= ni < N and 0 <= nj < N:
                height2 = array[ni][nj]
                weight = value + 1

                if height2 > height1:
                    weight += height2 - height1

                if dist[ni][nj] > weight:
                    dist[ni][nj] = weight
                    heappush(heap, (weight, ni, nj))

    print(f'#{tc} {dist[-1][-1]}')