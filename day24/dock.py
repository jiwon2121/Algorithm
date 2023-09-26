import sys
sys.stdin = open('./5202_input.txt')



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    s_e = [list(map(int, input().split())) for _ in range(N)]
    s_e.sort(key = lambda x : x[1])
    result = [s_e[0]]

    for se in s_e[1:]:
        if result[-1][1] <= se[0]:
            result.append(se)

    print(f'#{tc} {len(result)}')
