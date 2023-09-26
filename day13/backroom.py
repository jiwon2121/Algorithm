import sys

sys.stdin = open('./sample_input.txt')


def backroom(n, arr):
    max_count = 0
    count = [0 for _ in range(201)]

    for i in range(N):
        start = (arr[i][0]+1) // 2
        end = (arr[i][1]+1) // 2

        if end < start:
            start, end = end, start

        for j in range(start, end + 1):
            count[j] += 1
            if max_count < count[j]:
                max_count = count[j]

    return max_count

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    ans = backroom(N, array)
    print(f'#{tc} {ans}')

