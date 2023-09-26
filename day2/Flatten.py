import sys

def flatten(dump, boxes):
    height_lst = [0 for _ in range(100)]
    max_idx = 99
    min_idx = 0

    for box in boxes:
        height_lst[box - 1] += 1

    # print(height_lst)
    count = 0

    while True:
        while height_lst[max_idx] == 0:
            max_idx -= 1

        while height_lst[min_idx] == 0:
            min_idx += 1

        if (max_idx - min_idx == 1) or (count == dump):
            break

        height_lst[max_idx] -= 1
        height_lst[max_idx - 1] += 1

        height_lst[min_idx] -= 1
        height_lst[min_idx + 1] += 1

        count += 1

    diff = max_idx - min_idx
    return diff


sys.stdin = open('./input1.txt')

for i in range(1, 11):
    N = int(input())
    yellow_box = list(map(int, input().split()))
    result = flatten(N, yellow_box)

    print(f'#{i} {result}')