import sys
sys.stdin = open('./5178_input.txt')

def node_sum(node = 1):
    if node > N:
        return 0

    if tree[node] != 0:
        return tree[node]

    left = node_sum(node * 2)
    right = node_sum(node*2 +1)
    tree[node] = left + right
    return tree[node]


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    node_sum()
    print(f'#{tc} {tree[L]}')