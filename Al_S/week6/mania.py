import sys
from collections import deque


N = int(sys.stdin.readline())
tree = deque([[] for _ in range(N + 1)])
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0 for _ in range(N + 1)]
cnt = 0
st = deque([1])
visited[1] = 1

while st:
    root = st[-1]
    while tree[root]:
        child = tree[root].pop()
        if not visited[child]:
            break
        else:
            child = 0

    if child:
        st.append(child)
        visited[child] = 1

    else:
        st.pop()
        if st:
            ch_n = visited[root]
            cnt += ch_n * (ch_n - 1) // 2 + ch_n * (N - ch_n)
            visited[st[-1]] += ch_n

print(cnt)