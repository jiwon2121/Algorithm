from collections import deque

# input
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# water에 인접한 물의 수 저장
water = [[0 for _ in range(m)] for _ in range(n)]
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# ice에 빙산 위치를 저장
ice = []

# 빙산 위치를 ice에 append
for i, row in enumerate(array):
    for j, ele in enumerate(row):
        if ele != 0:
            w = 0

            for d1, d2 in delta:
                ni = i + d1
                nj = j + d2
                if 0 <= ni < n and 0 <= nj < m and array[ni][nj] == 0:
                    w += 1

            ice.append([i, j])
            water[i][j] = w

result = 1
l = len(ice)
while True:
    melt = []   # 다 녹은 빙산의 위치를 melt에 저장
    idx = 0     # idx는 ice의 idx
    while idx < l:
        i, j = ice[idx]
        value = array[i][j]     # value = 빙산 높이
        # 다 녹았다면
        if value - water[i][j] <= 0:
            array[i][j] = 0
            melt.append(ice.pop(idx))
            l -= 1
        # 녹지 않았다면
        else:
            array[i][j] = value - water[i][j]
            idx += 1
    # 빙산이 1개 이하면 무조건 한조각이므로 result = 0
    if l <= 1:
        result = 0
        break

    # bfs로 빙산이 한 조각인지 확인
    if melt:
        visited = [[0 for _ in range(m)] for _ in range(n)]
        que = deque()
        que.append(ice[0])
        visited[ice[0][0]][ice[0][1]] = 1
        cnt = 1
        while que:
            curr = que.popleft()
            for d1, d2 in delta:
                ni = d1 + curr[0]
                nj = d2 + curr[1]
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and array[ni][nj] != 0:
                    que.append([ni, nj])
                    visited[ni][nj] = 1
                    cnt += 1
        # 한조각이 아니면 break
        if cnt != l:
            break
        # 녹은 빙산 위치를 주위의 water +1
        for mel in melt:
            for d1, d2 in delta:
                ni = d1 + mel[0]
                nj = d2 + mel[1]
                if 0 <= ni < n and 0 <= nj < m:
                    water[ni][nj] += 1

    result += 1

print(result)