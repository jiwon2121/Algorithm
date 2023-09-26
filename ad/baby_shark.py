from heapq import heappush, heappop
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
size = 2
count = 0
fish = 0
time = 0
dist = 0

for i in range(N):
    for j in range(N):
        if array[i][j] == 9:
            curr = [i, j]
            array[i][j] = 0
        elif array[i][j] != 0:
            fish += 1

delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]
que = []
que2 = []
visited = [curr]
for d1, d2 in delta:
    ni = curr[0] + d1
    nj = curr[1] + d2
    if 0 <= ni < N and 0 <= nj < N and array[ni][nj] <= size:
        heappush(que, [ni, nj])
        visited.append([ni, nj])

while que:
    dist += 1
    while que:
        nxt = heappop(que)
        if 0 < array[nxt[0]][nxt[1]] < size:
            array[nxt[0]][nxt[1]] = 0
            curr = nxt
            fish -= 1
            count += 1
            time += dist
            dist = 0
            if count == size:
                size += 1
                count = 0

            que2.clear()
            visited.clear()
            visited.append(curr)
            for d1, d2 in delta:
                ni = curr[0] + d1
                nj = curr[1] + d2
                if 0 <= ni < N and 0 <= nj < N and array[ni][nj] <= size:
                    heappush(que2, [ni, nj])
                    visited.append([ni, nj])

            break

        for d1, d2 in delta:
            ni = nxt[0] + d1
            nj = nxt[1] + d2
            if 0 <= ni < N and 0 <= nj < N and array[ni][nj] <= size and [ni, nj] not in visited:
                heappush(que2, [ni, nj])
                visited.append([ni, nj])

    if fish == 0:
        break

    que = que2[::]
    que2.clear()

print(time)
