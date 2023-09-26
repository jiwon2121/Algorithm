import sys

sys.stdin = open('./5097_input.txt')

def rotation(n, m, arr):
    r = m % n
    return arr[r]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    ans = rotation(N, M, array)
    print(f'#{tc} {ans}')