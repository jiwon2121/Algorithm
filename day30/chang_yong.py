import sys
sys.stdin = open('./s_input.txt')

def find(x):
    p = parent[x]
    while p != x:
        x = p
        p = parent[x]

    return p

def union(x, y):
    x = find(x)
    y = find(y)
    p = min(x, y)

    parent[x] = p
    parent[y] = p

    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [n for n in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    result = set()
    for i in range(1, N+1):
        result.add(find(i))

    print(f'#{tc} {len(result)}')
