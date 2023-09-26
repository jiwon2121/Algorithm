import sys

def cut(brackets):
    # idx_st = [0 for _ in range(100001)]
    count = 0
    point = -1

    for i, b in enumerate(brackets):
        if b == '(':
            point += 1
            # idx_st[point] = i

        elif b == ')' and point > -1:
            # if i - idx_st[point] == 1:
            if brackets[i-1] == '(':
                count += point

            else:
                count += 1

            point -= 1

    return count


sys.stdin = open('./sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    brackets = input()
    result = cut(brackets)
    print(f'#{tc} {result}')