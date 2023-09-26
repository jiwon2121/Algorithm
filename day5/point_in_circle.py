import sys

def cnt_point(n):
    count = 0
    for i in range(n):
        length = (n ** 2 - i ** 2) ** (1/2)
        count += int(length)

    return count * 4 + 1



sys.stdin = open('./sample_input2.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = cnt_point(N)
    print(f'#{tc} {result}')