def prefix_sum(n, m, num_lst):
    max_sum = 0
    min_sum = 500000
    for i in range(0, n - m + 1):
        sum_tmp = 0

        for j in range(0, m):
            sum_tmp += num_lst[i + j]

        if sum_tmp > max_sum:
            max_sum = sum_tmp

        if sum_tmp < min_sum:
            min_sum = sum_tmp

    return max_sum - min_sum


T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    result = prefix_sum(N, M, numbers)
    print(f'#{tc} {result}')
