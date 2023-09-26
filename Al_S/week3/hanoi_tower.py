def hanoi(start, end, height):
    another = 6 - start - end

    if height == 1:
        arr.append([start, end])
        return 1

    n1 = hanoi(start, another,height - 1)
    n2 = hanoi(start, end, 1)
    n3 = hanoi(another, end, height - 1)

    return n1 + n2 + n3

def hanoi2(height):
    if height == 1:
        memo[height] = 1
        return 1

    if not memo[height - 1]:
        hanoi2(height - 1)

    memo[height] = memo[height - 1] * 2 + 1

    return memo[height]


K = int(input())
if K > 20:
    is_print = False

else:
    is_print = True

arr = []
memo = [False for _ in range(101)]


if is_print:
    ans = hanoi(1, 3, K)

    print(ans)
    for a in arr:
        print(*a)

else:
    ans = hanoi2(K)
    print(ans)