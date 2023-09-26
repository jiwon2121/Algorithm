def game(arr, count = 0):
    if count == 5:
        global max_num
        for row in arr:
            m = max(row)
            max_num = max(m, max_num)
        return

    ## 왼쪽
    moved = [[0 for _ in range(N)] for _ in range(N)]
    for i, row in enumerate(arr):
        que = []
        for ele in row:
            if ele != 0:
                que.append(ele)

        idx = 0
        while que:
            if len(que) == 1:
                moved[i][idx] = que.pop(0)
                break

            if que[0] == que[1]:
                moved[i][idx] = que.pop(0) * 2
                que.pop(0)
                idx += 1

            else:
                moved[i][idx] = que.pop(0)
                idx += 1

    game(moved, count + 1)

    ## 오른쪽
    moved = [[0 for _ in range(N)] for _ in range(N)]
    for i, row in enumerate(arr):
        que = []
        for ele in row[::-1]:
            if ele != 0:
                que.append(ele)

        idx = N - 1
        while que:
            if len(que) == 1:
                moved[i][idx] = que.pop(0)
                break

            if que[0] == que[1]:
                moved[i][idx] = que.pop(0) * 2
                que.pop(0)
                idx -= 1

            else:
                moved[i][idx] = que.pop(0)
                idx -= 1

    game(moved, count + 1)

    ## 위쪽
    moved = [[0 for _ in range(N)] for _ in range(N)]
    for j, col in enumerate(zip(*arr)):
        que = []
        for ele in col:
            if ele != 0:
                que.append(ele)

        idx = 0
        while que:
            if len(que) == 1:
                moved[idx][j] = que.pop(0)
                break
            if que[0] == que[1]:
                moved[idx][j] = que.pop(0) * 2
                que.pop(0)
                idx += 1

            else:
                moved[idx][j] = que.pop(0)
                idx += 1

    game(moved, count + 1)

    ## 아래쪽
    moved = [[0 for _ in range(N)] for _ in range(N)]
    for j, col in enumerate(zip(*arr)):
        que = []
        for ele in col[::-1]:
            if ele != 0:
                que.append(ele)

        idx = N - 1
        while que:
            if len(que) == 1:
                moved[idx][j] = que.pop(0)
                break
            if que[0] == que[1]:
                moved[idx][j] = que.pop(0) * 2
                que.pop(0)
                idx -= 1

            else:
                moved[idx][j] = que.pop(0)
                idx -= 1
    game(moved, count + 1)

    return


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
game(array)
print(max_num)