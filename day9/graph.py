import sys

def is_go(v, path, start, end):
    line = [[] for _ in range(v + 1)]

    for p in path:
        line[p[0]].append(p[1])

    visited = [0 for _ in range(v + 1)]
    st = [None for _ in range(len(path))]
    st[0] = start
    visited[start] = 1
    point = 0
    node = start

    while point > -1:
        for next in line[node]:
            if visited[next] == 0:
                node = next
                visited[node] = 1
                point += 1
                st[point] = node
                break

        else:
            point -= 1
            node = st[point]

        if st[point] == end:
            return 1

    return 0



sys.stdin = open('./4871_input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    path = []
    for _ in range(E):
        path.append(list(map(int, input().split())))

    start, end = map(int, input().split())

    result = is_go(V, path, start, end)

    print(f'#{tc} {result}')


