import sys
sys.stdin = open('./5207_input.txt')


def bin_search(key, l, r):
    # lc = 0
    # rc = 0
    ans = 0
    last = ''
    while l <= r:
        m = (l + r) // 2
        value = arr_n[m]

        if value == key:
            ans = 1
            break
        elif value < key:
            if last == 'right':
                break
            l = m + 1
            last = 'right'
        else:
            if last == 'left':
                break
            r = m - 1
            last = 'left'

    return ans

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_n = sorted(list(map(int, input().split())))
    arr_m = list(map(int, input().split()))
    cnt = 0
    for k in arr_m:
        cnt += bin_search(k, 0, N - 1)

    print(f'#{tc} {cnt}')
