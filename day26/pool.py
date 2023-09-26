import sys
sys.stdin = open('./sample_input.txt')


def pool(i = 0, total = 0):
    if i >= 12:
        global ans
        ans = min(ans, total)
        return

    if total >= ans:
        return

    for n in range(3):
        if n == 0:
            p = price[n] * use[i]
            pool(i+1, total+p)

        elif n == 1:
            pool(i+1, total+price[n])

        else:
            pool(i+3, total+price[n])

    return


T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    use = list(map(int, input().split()))
    ans = price[3]
    pool()
    print(f'#{tc} {ans}')
