import sys

sys.stdin = open('./input3.txt')

def contact(line, s):
    que = []
    calling = [0 for _ in range(101)]

    que.append(s)
    calling[s] += 1

    while que:
        node = que.pop(0)

        for next in line[node]:
            if not calling[next]:
                que.append(next)
                calling[next] = calling[node] + 1

    last_node = 0
    last_num = 1

    for i, n in enumerate(calling):
        if last_num <= n:
            last_num = n
            last_node = i

    return last_node


for tc in range(1, 11):
    N, S = map(int, input().split())
    adj = [[] for _ in range(101)]
    input_arr = list(map(int, input().split()))
    for i in range(0, N, 2):
        adj[input_arr[i]].append(input_arr[i + 1])


    print(f'#{tc} {contact(adj, S)}')
