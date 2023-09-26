import sys

def is_sudoku(arr):
    val = 1

    ### 가로 세로
    for i in range(9):
        row_count = [0 for _ in range(10)]
        col_count = [0 for _ in range(10)]
        for j in range(9):
            row_count[arr[i][j]] += 1
            col_count[arr[j][i]] += 1

        for ele in row_count:
           if ele > 1:
               val = 0
               return val

        for ele in col_count:
            if ele > 1:
                val = 0
                return val

    ### 박스
    for box in range(9):
        n = box // 3
        m = box % 3
        box_count = [0 for _ in range(10)]

        for i in range(3):
            for j in range(3):
                row = n * 3 + i
                col = m * 3 + j
                box_count[arr[row][col]] += 1

        for ele in box_count:
            if ele > 1:
                val = 0
                return val

    return val


sys.stdin = open('./input2.txt')

T = int(input())

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = is_sudoku(sudoku)

    print(f'#{tc} {result}')

