import sys
sys.stdin = open('./input1.txt')

def cal(node):
    value = array[node][0]
    if value in ['+', '-', '*', '/']:
        left = cal(int(array[node][1]))
        right = cal(int(array[node][2]))

        if value == '+':
            return left + right

        elif value == '-':
            return left - right

        elif value == '*':
            return left * right

        else:
            return left / right

    return int(value)


for tc in range(1, 11):
    N = int(input())
    array = [0]
    for _ in range(N):
        inp = list(input().split())
        array.append(inp[1:])

    ans = cal(1)
    print(f'#{tc} {int(ans)}')