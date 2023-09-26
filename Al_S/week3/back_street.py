from heapq import heappush, heappop

inf = 1e9
def dfs(n, start):
    st = []
    visited = [0] * (n + 1)
    st.append(start)
    visited[start] = 1
    while st:
        curr = st[-1]

        for i, c in enumerate(cost[curr]):
            if c != 0 and c != inf and not visited[i]:
                if i == n:
                    return True
                st.append(i)
                visited[i] = 1
                break

        else:
            st.pop()

    return False


def back_streeet(N):
    global inf
    max_cost = [[inf, []] for _ in range(N+1)]
    max_cost[1][0] = 0
    que = []
    max_cost[1][1].append(1)
    heappush(que, max_cost[1])

    while que:
        current, way = heappop(que)
        node = way[-1]
        current *= -1

        for i, c in enumerate(cost[node]):
            if c != inf and i != node:
                if i in way:
                    temp = current + max_cost[i][0]

                    if temp + c > 0:
                        if dfs(N, node):
                            print(-1)
                            return
                        max_cost[node][0] = -inf
                        continue

                if (-1) * max_cost[i][0] <= current + c:
                    max_cost[i][0] = (current + c)*(-1)
                    max_cost[i][1] = way + [i]
                    heappush(que, max_cost[i])

    if max_cost[N][0] == inf or max_cost[N][0] == -inf:
        print(-1)

    else:
        print(*max_cost[N][1])


N, M = map(int, input().split())
cost = [[inf for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    cost[i][i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    cost[u][v] = w

back_streeet(N)
