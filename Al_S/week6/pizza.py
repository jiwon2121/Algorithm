import sys

size = int(input())
m, n = map(int, input().split())

A = [int(sys.stdin.readline()) for _ in range(m)]
B = [int(sys.stdin.readline()) for _ in range(n)]

A_sum = {}
B_sum = {}

A_sum[0] = 1
if sum(A) <= size:
    A_sum[sum(A)] = 1

for i in range(0, m):
    s = 0
    for j in range(0, m-1):
        idx = (i + j) % m
        s += A[idx]
        if s > size:
            break
        A_sum[s] = A_sum.setdefault(s, 0) + 1

B_sum[0] = 1
if sum(B) <= size:
    B_sum[sum(B)] = 1

for i in range(0, n):
    s = 0
    for j in range(0, n-1):
        idx = (i + j) % n
        s += B[idx]
        if s > size:
            break
        B_sum[s] = B_sum.setdefault(s, 0) + 1

result = 0
# for k, a in A_sum.items():
#     remain = size - k
#     b = B_sum.get(remain, 0)
#     result += a * b

for i in range(0, size + 1):
    a = A_sum.get(i, 0)
    b = B_sum.get(size - i, 0)
    result += a * b

print(result)