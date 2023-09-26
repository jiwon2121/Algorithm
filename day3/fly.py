import sys

def kill_fly(n, m, arr):
    max_kill = 0

    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            kill = 0
            for mi in range(0, m):
                for mj in range(0, m):
                    kill += arr[i + mi][j + mj]

            if max_kill < kill:
                max_kill = kill

    return max_kill



sys.stdin = open('./input2.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    result = kill_fly(N, M, array)

    print(f'#{tc} {result}')