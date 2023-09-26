import sys
sys.stdin = open('./5174_input.txt')

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E + 2)]
    array = list(map(int, input().split()))
    for i in range(0, len(array), 2):
        idx, child = array[i], array[i+1]
        tree[idx].append(child)
    que = []
    que.append(N)
    count = 1
    while que:
        node = que.pop(0)
        for next in tree[node]:
            que.append(next)
            count += 1
    print(f'#{tc} {count}')