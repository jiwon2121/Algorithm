import sys

def facorization(num):
    prime = [0 for _ in range(12)]

    for i in [2, 3, 5, 7, 11]:
        while num % i == 0:
            num //= i
            prime[i] += 1

    return prime

sys.stdin = open('./input2.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    result = facorization(N)

    print(f'#{tc}', end = '')
    for i in [2, 3, 5, 7, 11]:
        print(f' {result[i]}', end = '')

    print()