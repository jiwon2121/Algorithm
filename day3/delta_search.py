import sys

def absolute(num):
    if num >= 0:
        return num

    return num * (-1)


def delta_search(n, arr):
    delta1 = [-1 ,0, 1, 0]
    delta2 = [0, 1, 0, -1]
    diff_sum = 0

    for i in range(n):
        for j in range(n):
            element = arr[i][j]

            for d1, d2 in zip(delta1, delta2):
                ni = i + d1
                nj = j + d2

                if (0 <= ni < n) and (0 <= nj < n):
                    tmp_diff = element - arr[ni][nj]
                    diff_sum += absolute(tmp_diff)

    return diff_sum

sys.stdin = open('./ex1_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    result = delta_search(N, array)
    print(f'#{tc} {result}')