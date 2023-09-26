def fibo(n):
    if n in memo:
        return

    st = [n]
    while st:
        curr = st[-1]
        flag = False
        m = curr // 2
        if curr % 2 == 0:
            n1 = m + 1
            n2 = m - 1
            if n1 not in memo:
                st.append(n1)
                flag = True
            if n2 not in memo:
                st.append(n2)
                flag = True
            if flag:
                continue
            memo[curr] = (memo[n1] ** 2 - memo[n2] ** 2) % 1000000000
            st.pop()

        else:
            n1 = m + 1
            n2 = m
            if n1 not in memo:
                st.append(n1)
                flag = True
            if n2 not in memo:
                st.append(n2)
                flag = True
            if flag:
                continue
            memo[curr] = (memo[n1] ** 2 + memo[n2] ** 2) % 1000000000
            st.pop()

    return
    # if n == 0:
    #     return 0
    # elif n == 1 or n == 2:
    #     return 1
    #
    # if n in memo:
    #     return memo[n]
    #
    # m = n // 2
    # if n % 2 == 0:
    #     result = (fibo(m+1) ** 2 - fibo(m - 1) ** 2) % 1000000000
    #     # result %= 1000000000
    #     memo[n] = result
    #     return result
    #
    # result = (fibo(m + 1) ** 2 + fibo(m) ** 2) % 1000000000
    # # result %= 1000000000
    # memo[n] = result
    # return result

# N = int(input())
N, M = map(int, input().split())
memo = {
    0 : 0,
    1 : 1,
    2 : 1
}

res = 0
for i in range(N, M, 2):
    fibo(i+2)
    res += memo[i+2]

if (M - N + 1) % 2 == 1:
    fibo(M)
    res += memo[M]

print(res % 1000000000)