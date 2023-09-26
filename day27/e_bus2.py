import sys
sys.stdin = open('./5208_input.txt')


def bus(stop=0, cnt=-1):
    global ans
    if stop >= N-1:
        ans = min(ans, cnt)
        return

    if cnt >= ans:
        return

    capa = array[stop]
    for i in range(1, capa + 1):
        bus(stop + i, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    N, *array = map(int, input().split())
    ans = 1e9
    bus()
    print(f'#{tc} {ans}')