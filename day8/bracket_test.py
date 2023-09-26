import sys

def bracket_test(string):
    st = []
    point = -1
    bracket_dict = {')' : '(', '}' : '{'}

    for s in string:
        if s in ['(', '{']:
            st.append(s)
            point += 1

        elif s in [')', '}']:
            if point == -1:
                return 0

            elif st[point] == bracket_dict[s]:
                st.pop()
                point -= 1

            else:
                return 0

    if point == -1:
        return 1

    return 0






sys.stdin = open('./4866_input.txt')

T = int(input())

for tc in range(1, T + 1):
    string = input()

    ans = bracket_test(string)
    print(f'#{tc} {ans}')