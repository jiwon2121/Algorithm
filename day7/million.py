import sys

def project(arr, n, start = 0):
    if start >= n-1:
        return 0

    max_price = 0
    max_idx = 0

    for i in range(start, n):
        if max_price < arr[i]:
            max_price = arr[i]
            max_idx = i


    total = 0
    for i in range(start, max_idx):
        total += max_price - arr[i]

    return total + project(arr,n, start = max_idx + 1)


sys.stdin = open('./input3.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    result = project(price, N)

    print(f'#{tc} {result}')


