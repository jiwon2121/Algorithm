import sys
sys.stdin = open('./sample_input.txt')


delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    array = [list(map(float, input().split())) for _ in range(N)]

    pops = [[] for _ in range(4001)]
    for i in range(N):
        x1, y1, d1, e1 = array[i]
        for j in range(i + 1, N):
            x2, y2, d2, e2 = array[j]
            dist1 = int(abs(x1 - x2) + abs(y1 - y2))
            dist2 = dist1 / 2
            nx1 = x1 + delta[int(d1)][0] * dist2
            ny1 = y1 + delta[int(d1)][1] * dist2
            nx2 = x2 + delta[int(d2)][0] * dist2
            ny2 = y2 + delta[int(d2)][1] * dist2

            if nx1 == nx2 and ny1 == ny2:
                pops[dist1].append((i, j))
    ext = set()
    for pop in pops:
        temp = set()
        for i, j in pop:
            if i not in ext and j not in ext:
                if i not in temp:
                    temp.add(i)
                    cnt += int(array[i][3])
                if j not in temp:
                    temp.add(j)
                    cnt += int(array[j][3])
        ext.update(temp)

    print(f'#{tc} {cnt}')