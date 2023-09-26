import sys

def my_sort(arr):
    new_arr = []
    cnt = 0

    for row in arr:
        for element in row:
            new_arr.append(element)
            cnt += 1

    for i in range(cnt):
        min_idx = i

        for j in range(i, cnt):
            if new_arr[min_idx] > new_arr[j]:
                min_idx = j

        new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]

    return new_arr

def snail_sort(n,arr):
    result = [[0 for _ in range(n)] for _ in range(n)]
    new_arr = my_sort(arr)

    i = 0
    j = -1
    cnt = 0
    delta1 = [0, -1, 0, 1]
    delta2 = [1, 0, -1, 0]
    num = 0

    while num <= n ** 2 - 1:
        d1 = delta1[cnt % 4]
        d2 = delta2[cnt % 4]

        while (0 <= i + d1 < n) and (0 <= j + d2 < n) and (result[i + d1][j + d2] == 0):
            i += d1
            j += d2
            result[i][j] = new_arr[num]

            num += 1

        cnt += 1

    return result




sys.stdin = open('./input4.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    result = snail_sort(N, array)

    print(f'#{tc}')
    for row in result:
        print(*row)