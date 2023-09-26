import sys


def is_bracket(string):
    st = []
    point = -1

    for b in brackets:
        if b == '(':
            st.append(b)
            point += 1

        elif b == ')':
            if point == -1:
                return -1

            else:
                st.pop()
                point -= 1

    if point != -1:
        return -1

    return 1



sys.stdin = open('./input2.txt')

T = int(input())

for tc in range(1, T+1):
    brackets = input()

    ans = is_bracket(brackets)
    print(f'#{tc} {ans}')
