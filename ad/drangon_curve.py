from copy import deepcopy
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

base = [[(0, 0), (1, 0)], [(0, 0), (0, -1)], [(0, 0), (-1, 0)], [(0, 0), (0, 1)]]
curve = []
for x, y, d, g in array:
    gen = 0
    curve_temp = deepcopy(base[d])

    while gen < g:
        i, j = curve_temp[-1]
        for m, n in curve_temp[-2::-1]:
            tup = (-(n-j)+i, m-i+j)
            curve_temp.append(tup)
        gen += 1

    for c in curve_temp:
        tup = (c[0] + x, c[1] + y)
        if tup not in curve:
            curve.append(tup)

cnt = 0
curve.sort()
for i, j in curve:
    if (i, j) in curve and (i+1, j) in curve and (i, j+1) in curve and (i+1, j+1) in curve:
        cnt += 1

print(cnt)