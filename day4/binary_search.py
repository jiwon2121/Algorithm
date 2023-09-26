import sys

def binary_search(start, end, key, count = 0):
    count += 1
    mid = (start + end) // 2

    if mid == key:
        return count

    elif mid < key:
        return binary_search(mid + 1, end, key, count)

    elif mid > key:
        return binary_search(start, mid - 1, key, count)


def game(p, pa, pb):
    a_count = binary_search(1, p, pa)
    b_count = binary_search(1, p, pb)

    if a_count > b_count:
        return 'B'

    elif a_count < b_count:
        return 'A'

    else:
        return 0




sys.stdin = open('./4839_input.txt')

T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int,input().split())

    result = game(P, Pa, Pb)

    print(f'#{tc} {result}')