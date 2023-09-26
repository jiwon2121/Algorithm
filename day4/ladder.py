import sys

def ladder(arr):
    for i, num in enumerate(arr[-1]):
        if num == 2:
            line_num = i
            break

    for row in arr[98::-1]:
        tmp_line = line_num
        for delta in [-1, 1]:
            nj = line_num

            while (0 <= nj + delta <= 99) and (row[nj + delta] == 1):

                nj += delta

                tmp_line = nj

        line_num = tmp_line

    return line_num


sys.stdin = open('./input1.txt')

for _ in range(10):
    tc = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    result = ladder(array)
    print(f'#{tc} {result}')

