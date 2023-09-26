import sys
sys.stdin = open('./re_sample_input.txt')
# sys.stdin = open('./text.txt')

def find(x):
    p = parent[x]
    while p != x:
        x = p
        p = parent[x]
    return p

def union(x, y):
    x = find(x)
    y = find(y)
    p = min(x, y)

    parent[x] = p
    parent[y] = p

    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xy = [[0, 0] for _ in range(N)]

    for i, x in enumerate(map(int, input().split())):
        xy[i][0] = x

    for i, y in enumerate(map(int, input().split())):
        xy[i][1] = y

    E = float(input())

    parent = [n for n in range(N)]
    edge = [0 for _ in range(N * (N - 1) // 2)]
    idx = 0

    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            c = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * E
            # cost[i][j] = c
            # cost[j][i] = c
            edge[idx] = (c, i, j)
            idx += 1
    edge.sort()

    cnt = 0
    res = 0
    for c, f, t in edge:
        if find(f) != find(t):
            cnt += 1
            res += c
            union(f, t)

            if cnt == N:
                break

    print(f'#{tc} {res:.0f}')

