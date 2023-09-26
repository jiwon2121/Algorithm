import sys
sys.stdin = open('./5209_input.txt')


def factory(i=0, total=0, used=0):
    global cost
    if i == N:
        cost = min(cost, total)
        return

    for j in range(N):
        if not used & 1 << j:
            c = V[i][j]
            if total + c < cost:
                factory(i+1, total+c, used | 1 <<j)

    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    cost = 1e9
    factory()
    print(f'#{tc} {cost}')
