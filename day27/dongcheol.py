import sys
sys.stdin = open('./input1.txt')


def distrib(i=0, total=1, used=0):
    global prob
    if i == N:
        prob = max(prob, total)
        return

    for j in range(N):
        if not used & 1 << j:
            p = array[i][j] / 100
            if total * p > prob:
                distrib(i+1, total * p, used | 1 << j)

    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    prob = 0
    distrib()
    prob *= 100
    print(f'#{tc} {prob:.6f}')