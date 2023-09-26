import sys

# def pascal_tri(n):
#     global arr
#     if n == 1:
#         arr[0].append(1)
#
#     else:
#         if not arr[n-2]:
#             pascal_tri(n-1)
#
#         for i in range(0, n):
#             if i == 0 or i == n-1:
#                arr[n-1].append(1)
#
#             else:
#                 value = arr[n-2][i-1] + arr[n-2][i]
#                 arr[n-1].append(value)

def pascal_tri(n):
    arr = []
    if n == 1:
        arr.append(1)
        print(*arr)
        return arr

    sub_arr = pascal_tri(n-1)

    for i in range(n):
        if i == 0 or i == n - 1:
            arr.append(1)
        else:
            arr.append(sub_arr[i-1] + sub_arr[i])

    print(*arr)
    return arr


sys.stdin = open('./input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # arr = [[] for _ in range(N)]
    # pascal_tri(N)

    print(f'#{tc}')
    # for line in arr:
    #     print(*line)
    pascal_tri(N)
