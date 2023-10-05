import sys

sys.stdin = open('input.txt')
def bf():
    for i in range(N):
        for j in range(2*M+W):
            s, e, t = edge[j]
            if time[e] > time[s] + t:
                if i == N-1:
                    return "YES"
                
                time[e] = time[s] + t
    return "NO"

TC = int(input())
inf = 1e9
for _ in range(TC):
    N, M, W = map(int, input().split())
    edge = []
    time = [inf for _ in range(N+1)]
    time[1] = 0

    for _ in range(M):
        S, E, T = map(int, input().split())
        edge.append((S, E, T))
        edge.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        edge.append((S, E, -T))

    print(bf())