import sys
sys.stdin = open('./input.txt')

def game(c):
    point = 0
    c_idx = 9
    count_lst = [0 for _ in range(10)]
    for i, n in enumerate(nums):
        count_lst[n] += 1

    while c != 0 and point < len(nums) - 1:
        count = count_lst[c_idx]
        if count:
            if c > count:
                move = count
            else:
                move = c

            num_idx = []
            for i, n in enumerate(nums):
                if n == c_idx:
                    num_idx.append(i)

            temp = []
            for t in range(count):
                if nums[point + t] == c_idx:
                    num_idx.remove(point + t)
                else:
                    temp.append([nums[point + t], point + t])

            temp.sort(reverse = True)

            for i in range(len(temp)):
                nums[temp[i][1]], nums[num_idx[i]] = nums[num_idx[i]], nums[temp[i][1]]

            c -= len(temp)
        point += count
        c_idx -= 1

    if c != 0:
        if max(count_lst) == 1 and c % 2 == 1:
            nums[-1], nums[-2] = nums[-2], nums[-1]


T = int(input())
for tc in range(1, T + 1):
    nums, change = input().split()
    nums = list(map(int, nums))
    # sorted_lst = sorted(nums, reverse = True)
    change = int(change)
    game(change)

    nums = list(map(str, nums))
    nums = int(''.join(nums))
    print(f'#{tc} {nums}')

