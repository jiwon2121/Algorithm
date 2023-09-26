def n_queen(used, row=1):
    if row == N:
        global cnt
        cnt += 1
        return

    for col in range(N):
        if used & 1 << col:
           continue

        flag = False
        for ii, jj in enumerate(coor[:row]):
            if abs(ii - row) == abs(jj - col):
                flag = True
                break
        if flag:
            continue

        coor[row] = col
        n_queen(used | 1 << col, row+1)

    return

N = int(input())
coor = [None for _ in range(N)]
cnt = 0
for c in range(N):
    coor[0] = c
    n_queen(1 << c)

print(cnt)