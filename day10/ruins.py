import sys

def find_relics(n, m):
    global array
    max_length = 0
    count = 0

    for i in range(n):
        for j in range(m):
            if array[i][j]:
                count += 1
            else:
                if max_length < count:
                    max_length = count
                count = 0

        else:
            if max_length < count:
                max_length = count
            count = 0

    for j in range(m):
        for i in range(n):
            if array[i][j]:
                count += 1
            else:
                if max_length < count:
                    max_length = count
                count = 0

        else:
            if max_length < count:
                max_length = count
            count = 0

    return max_length



sys.stdin = open('./input1.txt')

T = int(input())

array = [[0 for _ in range(100)] for _ in range(100)]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    for i in range(N):
        for j, value in enumerate(map(int, input().split())):
            array[i][j] = value

    result = find_relics(N, M)

    print(f'#{tc} {result}')

