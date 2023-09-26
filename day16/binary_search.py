import sys
sys.stdin = open('./5176_input.txt')

def binary_search(N, node = 1):
    if not (1 <= node <= N):
        return

    binary_search(N, node * 2)
    result[node] = numbers.pop(0)
    binary_search(N, node * 2 + 1)
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(range(1, N+1))
    result = [0 for _ in range(N+1)]
    binary_search(N)

    print(f'#{tc} {result[1]} {result[N//2]}')
