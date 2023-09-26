import sys
sys.stdin = open('./input.txt')

def babygin(arr):
    uniq = set(arr)
    cnt = 0

    for u in uniq:
        if arr.count(u) == 3:
            cnt += 1
            idx = arr.index(u)
            arr.pop(idx)
            arr.pop(idx)
            arr.pop(idx)

    for i in range(0, len(arr), 3):
        num = arr[i]
        for j in range(1, 3):
            if arr[i + j] != num + j:
                break
        else:
            cnt += 1

    if cnt == 2:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    array = sorted(list(map(int, input())))
    print(f'#{tc} {babygin(array)}')

