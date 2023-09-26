import sys
sys.stdin = open('./sample_input.txt')

def omok(n, arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for d1, d2 in [[1, 0], [0, 1], [1, 1], [1, -1]]:
                    ni = i
                    nj = j
                    count = 0
                    while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                        count += 1
                        ni += d1
                        nj += d2

                    if count == 5:
                        print('Yes')
                        return

    print('No')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [list(input()) for _ in range(N)]
    print(f'#{tc}', end = ' ')
    omok(N, array)