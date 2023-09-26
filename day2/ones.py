import sys

def ones(number):
    max_len = 0

    count = 0
    for n in number:
        if n == 1:
            count += 1

        else:
            if count > max_len:
                max_len = count

            count = 0

    if count > max_len:
        max_len = count

    return max_len

sys.stdin = open('./input3.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    result = ones(arr)

    print(f'#{tc} {result}')
