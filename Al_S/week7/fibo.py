def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    if n in memo:
        return memo[n]

    m = n // 2
    if n % 2 == 0:
        result = fibo(m+1) ** 2 - fibo(m - 1) ** 2
        result %= 1000000007
        memo[n] = result
        return result

    result = fibo(m + 1) ** 2 + fibo(m) ** 2
    result %= 1000000007
    memo[n] = result
    return result

N = int(input())
memo = {}
print(fibo(N))

