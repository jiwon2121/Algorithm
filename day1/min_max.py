def min_max(num_lst):
    min_n = 1000000
    max_n = 1

    for num in num_lst:
        if num < min_n:
            min_n = num

        if num > max_n:
            max_n = num

    return min_n, max_n


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_num, max_num = min_max(numbers)

    print(f'#{tc} {max_num - min_num}')
