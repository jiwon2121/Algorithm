import sys

sys.stdin = open('./5099_input.txt')

def pizza(n, m, arr):
    pit = [[] for _ in range(n)]

    for i in range(n):
        pit[i].extend([i + 1, arr[i] // 2])

    p = n
    pop_count = 0
    while True:
        for i in range(n):
            if pit[i]:
                if pit[i][1] == 0:
                    if p < m:
                        pit[i][0] = p + 1
                        pit[i][1] = arr[p] // 2
                        p += 1
                        pop_count += 1

                    else:
                        pit[i] = []
                        pop_count += 1
                else:
                    pit[i][1] //= 2

            if pop_count == m-1:
                for i in range(n):
                    if pit[i]:
                        return pit[i][0]


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    ans = pizza(N, M, array)

    print(f'#{tc} {ans}')
