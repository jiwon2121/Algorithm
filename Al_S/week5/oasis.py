import sys
from collections import deque

N = int(input())
st = deque()
num = int(sys.stdin.readline())
st.append([num, 1])
result = 0

for _ in range(1, N):
    num = int(sys.stdin.readline())
    cnt = 1
    while st:
        top_n = st[-1][0]
        if top_n < num:
            result += st.pop()[1]
        elif top_n == num:
            cnt += st.pop()[1]
            result += cnt - 1
        else:
            result += 1
            break

    st.append([num, cnt])

print(result)