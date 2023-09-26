import sys

def snail(n):
    result = [[0 for _ in range(n)] for _ in range(n)]

    i = 0
    j = -1
    count = 0
    delta1 = [0, -1, 0, 1]
    delta2 = [1, 0, -1, 0]
    num = 1

    while num <= n**2:
        d1 = delta1[count % 4]
        d2 = delta2[count % 4]

        while (0 <= i + d1 < n) and (0 <= j + d2 < n) and (result[i+d1][j+d2] == 0):
            i += d1
            j += d2
            result[i][j] = num

            num += 1

        count += 1

    return result




sys.stdin = open('./input3.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ans = snail(N)

    print(f'#{tc}')

    for row in ans:
        print(*row)
