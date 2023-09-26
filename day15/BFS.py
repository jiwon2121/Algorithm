import sys

sys.stdin = open('./input4.txt')

def bfs(v, line):
    que = []
    visited = [0 for _ in range(v + 1)]

    que.append(1)
    visited[1] = 1
    print(' 1', end = '')

    while que:
        node = que.pop(0)

        for next in line[node]:
            if not visited[next]:
                que.append(next)
                visited[next] = 1
                print(f' {next}', end = '')

    return


V, E = map(int, input().split())
inp = list(map(int, input().split()))
array = [[] for _ in range(V + 1)]
for i in range(0, 2 * E, 2):
    array[inp[i]].append(inp[i + 1])
    array[inp[i + 1]].append(inp[i])

print('#1', end = '')
bfs(V, array)