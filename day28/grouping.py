import sys
sys.stdin = open('./5248_input.txt')


def find(x):
    p = parent[x]
    while p != x:
        x = parent[x]
        p = parent[x]

    return p


def union(x, y):
    p1 = find(x)
    p2 = find(y)

    if p1 == p2:
        return
    # parent[max(x, y)] = min(x, y)
    p = min(p1, p2)
    parent[x] = p
    parent[y] = p
    parent[p1] = p
    parent[p2] = p
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [n for n in range(N+1)]
    array = list(map(int, input().split()))
    for i in range(M):
        n1 = array[2*i+1]
        n2 = array[2*i]
        union(n1, n2)

    s = set()
    for i in range(1, N+1):
        s.add(find(i))

    print(f'#{tc}', len(s))
    print(parent)
    print(s)
