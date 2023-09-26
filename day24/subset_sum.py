import sys
sys.stdin = open('./sample_input.txt')

def solution(start = 0, total = 0):
    global count
    if start == N:
        if total == K:
            count += 1
        return

    for i in range(start, N):
        if total + array[i] == K:
            count += 1
            continue
        elif total + array[i] > K:
            continue
        else:
            solution(i + 1, total + array[i])

    return


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    count = 0
    solution()

    print(f'#{tc} {count}')
