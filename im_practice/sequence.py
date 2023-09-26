N, K = map(int, input().split())
tmp = list(map(int, input().split()))

max_sum = sum(tmp[0 : K])
temp_sum = max_sum
for i in range(1, N - K + 1):
    temp_sum -= tmp[i-1]
    temp_sum += tmp[i + K - 1]
    max_sum = max(max_sum, temp_sum)

print(max_sum)