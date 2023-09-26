import sys
sys.stdin = open('./input1.txt')


def distrib(row = 0, used = 0):
    if used == (1 << N) - 1:
        return 1

    if dp[used] != None:
        return dp[used]

    temp = 0
    for i in range(N):
        if not used & 1 << i:
            value = distrib(row + 1, used | 1 << i)
            temp = max(temp, value * array[row][i]/100)

    dp[used] = temp
    return temp


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    dp = [None for _ in range(1<<N)]
    ans = distrib() * 100
    print(f'#{tc} {ans:.6f}')