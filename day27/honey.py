import sys
sys.stdin = open('./sample_input2.txt')


def max_sum(arr):
    l = len(arr)
    res = 0
    for s in range(1, 1 << l):
        sum1 = 0
        sum2 = 0
        for n in range(l):
            if s & 1 << n:
                sum1 += arr[n]
                sum2 += arr[n] ** 2

                if sum1 > C:
                    break

        else:
            res = max(res, sum2)

    return res


T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N - M + 1):
            total = max_sum(array[i][j:j+M])
            for i2 in range(i, N):
                for j2 in range(N - M + 1):
                    if not (i2 == i and (j <= j2 < j + M or j <= j2 + M < j + M)):
                        ans = max(ans, total + max_sum(array[i2][j2:j2+M]))


    print(f'#{tc}', ans)