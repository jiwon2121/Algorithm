import sys

def is_go(arr):
    line = [[] for _ in range(100)]

    i = 0
    while i < len(arr):
        line[arr[i]].append(arr[i+1])
        i += 2

    visited = [0 for _ in range(100)]
    st = [None for _ in range(len(line))]
    st[0] = 0
    visited[0] = 1
    point = 0
    node = 0

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

        if st[point] == 99:
            return 1

    return 0



sys.stdin = open('./input1.txt')

for _ in range(1, 11):
    tc, N = input().split()
    array = list(map(int, input().split()))

    result = is_go(array)

    print(f'#{tc} {result}')

