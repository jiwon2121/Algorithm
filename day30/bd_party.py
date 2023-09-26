import sys
# sys.stdin = open('./test.txt')
sys.stdin = open('./input.txt')

def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

    return


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    inf = 1e9
    adj = [[inf for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        adj[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x][y] = c

    floyd_warshall()
    result = 0

    for i in range(1, N+1):
        temp = adj[X][i] + adj[i][X]
        if temp < inf:
            result = max(result, temp)

    print(f'#{tc} {result}')


