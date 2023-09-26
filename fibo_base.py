def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    if n in memo:
        return memo[n]

    m = n // 2
    if n % 2 == 0:
        result = (fibo(m+1) ** 2 - fibo(m - 1) ** 2) % 1000000000
        # result %= 1000000000
        memo[n] = result
        return result

    result = (fibo(m + 1) ** 2 + fibo(m) ** 2) % 1000000000
    # result %= 1000000000
    memo[n] = result
    return result

# N = int(input())
N, M = map(int, input().split())
memo = {}


# res = 0
# for i in range(N, M, 2):
#     res += fibo(i+2)
#
# if (M - N + 1) % 2 == 1:
#     res += fibo(M)

print((fibo(M+2) - fibo(N+1)) % 1000000000)