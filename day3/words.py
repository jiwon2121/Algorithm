import sys

def words(n, k, arr):
    count = 0

    for i in range(n):
        row_tmp = []
        col_tmp = []
        row_len = 0
        col_len = 0

        for j in range(n):
            if arr[i][j] == 1:
                row_len += 1

            else:
                row_tmp.append(row_len)
                row_len = 0

            if arr[j][i] == 1:
                col_len += 1

            else:
                col_tmp.append(col_len)
                col_len = 0

        row_tmp.append(row_len)
        col_tmp.append(col_len)

        for num in row_tmp:
            if num == k:
                count += 1

        for num in col_tmp:
            if num == k:
                count += 1

    return count


sys.stdin = open('./input3.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    result = words(N, K, array)

    print(f'#{tc} {result}')