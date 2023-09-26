import sys

def gns(arr):
    gns_dict = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9
    }

    count_lst = [0 for _ in range(10)]
    sort_lst = []

    for num in arr:
        count_lst[gns_dict[num]] += 1

    for key, value in gns_dict.items():
        for i in range(count_lst[value]):
            sort_lst.append(key)

    return sort_lst


sys.stdin = open('./GNS_test_input.txt')

T = int(input())
for _ in range(T):
    tc, N = input().split()
    array = list(input().split())
    ans = gns(array)

    print(tc)
    print(*ans)

