def bingo():
    count = 0
    for n, c in enumerate(call):
        for i in range(5):
            for j in range(5):
                if board[i][j] == c:
                    row_check[i] += 1
                    col_check[j] += 1
                    if row_check[i] == 5:
                        count += 1
                    if col_check[j] == 5:
                        count += 1

                    if i == j:
                        cross_check[0] += 1
                        if cross_check[0] == 5:
                            count += 1

                    if i + j == 4:
                        cross_check[1] += 1
                        if cross_check[1] == 5:
                            count += 1

                    if count >= 3:

                        print(n+1)
                        return


board = [input().split() for _ in range(5)]
row_check = [0 for _ in range(5)]
col_check = [0 for _ in range(5)]
cross_check = [0, 0]
call = []
for _ in range(5):
    call.extend(input().split())
bingo()