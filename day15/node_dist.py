import sys

sys.stdin = open('./5102_input.txt')

def dist(v, line, s, g):
    que = []
    visited = [0 for _ in range(v + 1)]

    for next in line[s]:
        que.append(next)
        visited[next] += 1

    while que:
        node = que.pop(0)

        for next in line[node]:
            if visited[next] == 0:
                que.append(next)
                visited[next] = visited[node] + 1

    return visited[g]


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int,input().split())
    adj = [[] for _ in range(V + 1)]

    for _ in range(E):
        x, y = map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)

    S, G = map(int, input().split())

    print(f'#{tc} {dist(V, adj, S, G)}')

