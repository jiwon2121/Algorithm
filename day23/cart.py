import sys
sys.stdin = open('./5189_input.txt')

def cart(start = 0, dist = 0):
    global min_dist

    if sum(visited) == N:
        dist += adj[start][0]
        min_dist = min(min_dist, dist)
        return

    for end in range(1, N):
        if not visited[end]:
            if dist + adj[start][end] > min_dist:
                return
            visited[end] = 1
            cart(end, dist + adj[start][end])
            visited[end] = 0

    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    visited[0] = 1
    min_dist = 1000
    cart()
    print(f'#{tc} {min_dist}')