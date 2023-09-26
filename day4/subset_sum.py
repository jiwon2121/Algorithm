import sys

def subset_sum(n, k):
    arr = [x for x in range(1, 13)]
    subset_num = 1<<12
    count = 0

    for i in range(1, subset_num):
        bi_num = bin(i)
        one_count = 0
        total = 0

        for num in bi_num:
            if num == '1':
                one_count += 1

        if one_count == n:
            for j in range(i):
                if i & (1 << j):
                    total += arr[j]

            if total == k:
                count += 1

    return count


sys.stdin = open('./4837_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    result = subset_sum(N,K)

    print(f'#{tc} {result}')