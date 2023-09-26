N, M = map(int, input().split())
array = [list(input()) for _ in range(M)]
cnt_dict = {'W' : 0, 'B' : 0}
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(M):
    for j in range(N):
        if array[i][j]:
            color = array[i][j]
            que = [[i, j]]
            array[i][j] = 0
            count = 1

            while que:
                curr = que.pop(0)
                for d1, d2 in delta:
                    ni = curr[0] + d1
                    nj = curr[1] + d2
                    if 0 <= ni < M and 0 <= nj < N and array[ni][nj] == color:
                        que.append([ni, nj])
                        array[ni][nj] = 0
                        count += 1

            cnt_dict[color] += count ** 2

print(cnt_dict['W'], cnt_dict['B'])
