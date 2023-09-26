import sys
sys.stdin = open('./sample_input2.txt')

def secom(n,m,arr):
    house = []
    max_visit = 0
    l = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                house.append([i,j])
                l += 1

    for i in range(n):
        for j in range(n):
            count = {}
            for hi, hj in house:
                d = abs(hi - i) + abs(hj - j) + 1
                count[d] = count.get(d,0) + 1
            visit = 0
            for k in sorted(count.keys()):
                cost = k ** 2 + (k - 1) ** 2
                visit += count[k]
                profit = visit * m -cost
                if profit >= 0:
                    max_visit = max(max_visit, visit)

            if max_visit == l:
                return max_visit

    return max_visit


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    ans = secom(N,M,array)
    print(f'#{tc} {ans}')