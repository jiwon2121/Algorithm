# def number_sum(l, u):
#     diff = u - l
#
#     total = 0
#     i = 0
#     while u // (10 ** i) != 0:
#         right = l % (10 ** i)
#         left = l // (10 ** (i + 1))
#         middle = l // (10 ** i) % 10
#
#         diff_right = diff % (10 ** (i + 1))
#         diff_left = diff // (10 ** (i + 1))
#
#         total += diff_left * 45 * (10 ** i)
#         total += middle * (10 ** i - right)
#
#         if i == 0:
#             diff_remain = diff_right
#         else:
#             diff_remain = diff_right - (10 ** i - right)
#
#         for j in range(1, diff_remain // (10 ** i)):
#             middle += 1
#             total += (middle % 10) * (10 ** i)
#
#         middle += 1
#         total += middle * (diff_remain % (10 ** i) + 1)
#
#         i += 1
#
#     return total

def number_sum(l, u):
    total = 0
    diff = u - l
    num_str = f'{l:0>10}'
    num_lst = [int(x) for x in num_str[::-1]]
    position_sum = sum(num_lst)

    position_sum -= 1
    num_lst[0] -= 1
    for _ in range(diff + 1):
        i = 0
        position_sum += 1
        num_lst[i] += 1

        while num_lst[i] == 10:
            position_sum -= 9
            num_lst[i] = 0

            i+=1
            num_lst[i] += 1

        total += position_sum

    return total



L, U = map(int, input().split())
result = number_sum(L,U)

print(result)


