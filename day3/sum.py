import sys

def line_sum(arr):
    max_sum = 0
    # 합

    cross_r_sum = 0
    cross_l_sum = 0

    for i in range(100):
        row_sum = 0
        col_sum = 0

        cross_r_sum += arr[i][i]
        cross_l_sum += arr[99 - i][99 - i]

        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

        for s in [row_sum, col_sum]:
            if max_sum < s:
                max_sum = s

    for s in [cross_r_sum, cross_l_sum]:
        if max_sum < s:
            max_sum = s

    return max_sum


sys.stdin = open('./input1.txt')

for _ in range(10):
    T = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    result = line_sum(array)

    print(f'#{T} {result}')