def find_palindrome(n, m, arr):
    for i in range(n):
        for j in range(n - m + 1):
            row_str = ''
            col_str = ''
            for k in range(m):
                row_str += arr[i][j+k]
                col_str += arr[j+k][i]

            if row_str == row_str[::-1]:
                return row_str

            if col_str == col_str[::-1]:
                return col_str


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result = find_palindrome(N, M, arr)

    print(f'#{tc} {result}')