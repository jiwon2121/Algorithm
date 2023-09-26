import sys
sys.stdin = open('./input2.txt')

def lvr(tree, root = 1):
    left = None
    right = None
    result = []
    for i, num in enumerate(tree[root][1]):
        if i == 0:
            left = num

        else:
            right = num

    if left != None:
        result.extend(lvr(tree, left))

    result.append(tree[root][0][0])

    if right != None:
        result.extend(lvr(tree, right))

    return result


for tc in range(1, 11):
    N = int(input())
    tree = [[[], []] for _ in range(N + 1)]

    for _ in range(N):
        temp = list(input().split())
        for i, a in enumerate(temp):
            if i == 0:
                idx = int(a)

            elif i == 1:
                tree[idx][0].append(a)

            else:
                tree[idx][1].append(int(a))

    ans = ''.join(lvr(tree))

    print(f'#{tc} {ans}')