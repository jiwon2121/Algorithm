N = int(input())
array = [0 for _ in range(1001)]
for _ in range(N):
    i, h = map(int, input().split())
    array[i] = h

m = max(array)
left = None
right = None
h_max = 0
for i in range(1001):
    if array[i] == m:
        left = i
        break

    if h_max < array[i]:
        h_max = array[i]

    array[i] = h_max

h_max = 0
for i in range(1000, -1, -1):
    if array[i] == m:
        right = i
        break

    if h_max < array[i]:
        h_max = array[i]

    array[i] = h_max

for i in range(left, right + 1):
    array[i] = m

print(sum(array))