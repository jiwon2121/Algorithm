import sys

sys.stdin = open('./4881_input.txt')

def min_sum(array, n, row = 0, total = 0):
    global ans
    if row == n:
        if ans > total:
            ans = total
        return

    for i in range(n):
        if i in used_col:
            continue

        num = array[row][i]

        if total + num > ans:
            continue

        used_col.append(i)
        min_sum(array, n, row + 1, total + num)
        used_col.pop()

    return


T = int(input())

used_col = []

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    ans = 100

    min_sum(array, N)

    print(f'#{tc} {ans}')



