import sys
sys.stdin = open('./sample_input.txt')

def attach(row, col, cnt=1, num=0):
    global ans
    value = array[row][col]
    num = num * 10 + value

    if cnt == 7:
        ans.add(num)
        return

    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for d1, d2 in delta:
        ni = row + d1
        nj = col + d2
        if 0 <= ni < 4 and 0 <= nj < 4:
            attach(ni, nj, cnt+1, num)


T = int(input())
for tc in range(1, T + 1):
    array = [list(map(int, input().split())) for _ in range(4)]
    ans = set()

    for i in range(4):
        for j in range(4):
            attach(i, j)

    print(f'#{tc}', len(ans))
