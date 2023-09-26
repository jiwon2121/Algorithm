import sys


def power(o_f, c):
    if c == P:
        return 0

    if dp[o_f] != None:
        return dp[o_f]

    temp_value = 1e9
    for no in range(N):
        if not o_f & 1 << no:
            o_f2 = o_f | 1 << no
            for yes in range(N):
                if o_f & 1 << yes:
                    value = power(o_f2, c+1)
                    if value != 1e9:
                        temp_value = min(temp_value, value + cost[yes][no])

    dp[o_f] = temp_value

    return temp_value


N = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
on_off = 0
for i, s in enumerate(input()):
    if s == 'Y':
        on_off = on_off | 1 << i
        cnt += 1

P = int(input())
if P <= cnt:
    print(0)
else:
    dp = [None for _ in range((1 << N))]
    result = power(on_off, cnt)
    if result != 1e9:
        print(result)
    else:
        print(-1)
