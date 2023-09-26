import sys
sys.stdin = open('./sample_input2.txt')

def secom(n,m,arr):
    max_house = 0
    max_visit = 0
    house_num = 0
    k = 0

    for a in arr:
        house_num += sum(a)

    while max_visit != house_num:
        k += 1
        cost = k**2 + (k-1)**2
        visit = 0

        for row in range(n):
            for col in range(n):
                visit = 0

                for d1 in range(-(k-1), k):
                    dd = k-abs(d1)
                    for d2 in range(-(dd-1),dd):
                        ni = row + d1
                        nj = col + d2
                        if 0 <= ni < n and 0 <= nj < n:
                            visit += arr[ni][nj]

                profit = visit * m - cost

                if profit >= 0:
                    max_house = max(max_house, visit)

                max_visit = max(max_visit, visit)

    return max_house


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    ans = secom(N,M,array)
    print(f'#{tc} {ans}')
