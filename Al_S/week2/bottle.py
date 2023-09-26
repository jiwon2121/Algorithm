# def count_add(n, k):
#     if (n > 1e7) or (n <= 0) or (k > 1000) or (k <= 0):
#         return -1
#
#     count = 0
#     binary_n = bin(n + count)
#     bottle = binary_n.count('1')
#
#     while bottle > k:
#         count += 1
#         binary_n = bin(n + count)
#         bottle = binary_n.count('1')
#
#     return count
#
#
# N, K = list(map(int, input().split()))
#
# print(count_add(N, K))

def bottle(n, k):
    if (n >1e7) or (n <= 0) or (k > 1000) or (k <= 0):
        return -1

    bottle_bin = bin(n)