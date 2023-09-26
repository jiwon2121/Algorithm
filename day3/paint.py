import sys

def paint(array):
    violet = 0
    paper = [[0 for _ in range(10)] for _ in range(10)]

    for row in array:
        s_row, s_col, e_row, e_col, color = row

        for i in range(s_row, e_row + 1):
            for j in range(s_col, e_col + 1):
                if (paper[i][j] < 3) and (paper[i][j] != color):
                    paper[i][j] += color

                if paper[i][j] == 3:
                    violet += 1

    return violet

sys.stdin = open('./4836_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    result = paint(array)

    print(f'#{tc} {result}')
