import sys
sys.stdin = open('./5204_input.txt')


def merge(arr):
    l = len(arr)
    if l <= 1:
        return arr

    left = merge(arr[:l//2])
    right = merge(arr[l//2:])
    new = []

    left_len = l//2
    right_len = l - l//2

    i = 0
    j = 0

    while True:
        if i == left_len:
            new.extend(right[j:])
            break
        elif j == right_len:
            new.extend(left[i:])
            break

        if left[i] <= right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    if left[-1] > right[-1]:
        global cnt
        cnt += 1

    return new


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    cnt = 0

    sorted_arr = merge(array)
    print(f'#{tc}', sorted_arr[N//2], cnt)