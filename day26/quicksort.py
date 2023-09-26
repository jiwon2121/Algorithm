import sys
sys.stdin = open('./5205_input.txt')


def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    eq = 1
    left = []
    right = []

    for num in arr[1:]:
        if num == pivot:
            eq += 1
        elif num < pivot:
            left.append(num)
        else:
            right.append(num)

    new = quick(left) + [pivot for _ in range(eq)] + quick(right)

    return new


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    sorted_arr = quick(array)
    print(f'#{tc}', sorted_arr[N//2])