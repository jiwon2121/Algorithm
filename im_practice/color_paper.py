N = int(input())
array = [None for _ in range(10000)]

count = 0
for _ in range(N):
    x, y = map(int, input().split())
    for x2 in range(x, x + 10):
        for y2 in range(y, y + 10):
            if [x2, y2] not in array:
                array[count] = [x2, y2]
                count += 1

print(count)




