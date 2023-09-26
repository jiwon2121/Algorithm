import sys

def attach(l):
    global arr
    if l == 1:
        arr.append([[1]])
        return

    result = []
    for i, element in enumerate(arr[l-1]):
        result.append([1] + element)

        if element[0] == 1:
            result.append([2] + element[1:])
            result.append([3] + element[1:])

    arr.append(result)

    return


sys.stdin = open('./4869_input.txt')

T = int(input())

arr = [[]]
length = 0

for tc in range(1, T + 1):
    N = int(input()) // 10

    while length < N:
        length += 1
        attach(length)

    print(f'#{tc} {len(arr[N])}')

