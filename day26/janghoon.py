import sys
sys.stdin = open('./input2.txt')


def solution(h=0, visited=0):
    if B <= h:
        return 0

    if dp[visited]:
        return dp[visited]

    temp = 1e9
    for i in range(N):
        if not visited & (1 << i):
            value = solution(h + height[i], visited | 1 << i)
            temp = min(temp, value + height[i])

    dp[visited] = temp
    return temp


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    dp = [0 for _ in range(1 << N)]
    ans = solution()
    print(f'#{tc} {ans - B}')