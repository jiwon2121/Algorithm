import sys
sys.stdin = open('./input.txt')

from heapq import heappop, heappush


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]
    dist = [[1e9 for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    heap = []
    heappush(heap, (0, 0, 0))

    while heap:
        value, i, j = heappop(heap)
        for d1, d2 in delta:
            ni = d1 + i
            nj = d2 + j
            if 0 <= ni < N and 0 <= nj < N:
                weight = value + array[ni][nj]
                if dist[ni][nj] > weight:
                    dist[ni][nj] = weight
                    heappush(heap, (weight, ni, nj))

    print(f'#{tc} {dist[-1][-1]}')