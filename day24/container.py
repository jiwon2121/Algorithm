import sys
sys.stdin = open('./5201_input.txt')

def go(wt, cp):
    used = [0 for _ in range(len(wt))]
    total = 0
    for c in cp:
        for i, w in enumerate(wt):
            if w <= c and not used[i]:
                total += w
                used[i] = 1
                break

    return total


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    capacity = sorted(list(map(int, input().split())), reverse=True)
    ans = go(weight, capacity)
    print(f'#{tc} {ans}')
