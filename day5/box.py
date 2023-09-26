import sys

def change(arr, i, l, r):
    for idx in range(l-1, r):
        arr[idx] = i



sys.stdin = open('./sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    array = [0 for _ in range(N)]

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        change(array, i, L, R)

    print(f'#{tc} ', end = '')
    print(*array)
