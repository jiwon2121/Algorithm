import sys

def subset(arr):
    subset_num = 1<<10
    is_val = False

    for i in range(1, subset_num):
        total = 0
        for j in range(10):
            if (1 << j) & i:
                total += arr[j]

        if not total:
            is_val = True

    return int(is_val)


sys.stdin = open('./input2.txt')

T = int(input())

for tc in range(1, T + 1):
    array = list(map(int, input().split()))
    result = subset(array)

    print(f'#{tc} {result}')