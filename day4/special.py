import sys

def special(n, arr):
    for i in range(n-1):
        # 홀수
        if i % 2:
            for j in range(n-2, i-1, -1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # 짝수
        else:
            for j in range(n-2, i-1, -1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


sys.stdin = open('./4843_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    special(N, array)

    print(f'#{tc}', end = ' ')
    print(*array[:10])