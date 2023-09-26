import sys

sys.stdin = open('./input2.txt')

def boong(n, m, k, arr):
    count_dict = {}
    total = 0
    for a in arr:
        key = a // m
        count_dict[key] = count_dict.get(key, 0) + 1

    for key in sorted(count_dict.keys()):
        made = key * k
        if made >= n:
            return 'Possible'

        total += count_dict[key]

        if total > made:
            return 'Impossible'

    return 'Possible'


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    costumer = list(map(int, input().split()))
    ans = boong(N, M, K, costumer)

    print(f'#{tc} {ans}')
