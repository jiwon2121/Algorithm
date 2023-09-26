import sys

def is_go(arr, v, e):
    i = 0
    line = [[] for _ in range(v + 1)]
    result = []

    while i < len(arr):
        line[arr[i]].append(arr[i+1])
        line[arr[i+1]].append(arr[i])
        i += 2

    visited = [0 for _ in range(100)]
    st = [None for _ in range(len(line))]
    st[0] = 1
    visited[1] = 1
    point = 0
    node = 1
    result.append(node)

    while point > -1:
        for next in line[node]:
            if visited[next] == 0:
                node = next
                result.append(node)
                visited[node] = 1
                point += 1
                st[point] = node
                break

        else:
            point -= 1
            node = st[point]

    return result


sys.stdin = open('./input2.txt')


V, E = map(int, input().split())
array = list(map(int, input().split()))
result = is_go(array, V, E)

print('#1', end = ' ')
print(*result , sep = '-')
