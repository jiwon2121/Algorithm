import sys

sys.stdin = open('./input1.txt')

def calculator(problem):
    st = []
    result = []
    cal_dict = {
        '+' : 1,
        '*' : 2
    }

    for p in problem:
        if p not in cal_dict.keys():
            result.append(int(p))

        else:
            while st and cal_dict[st[-1]] >= cal_dict[p]:
                result.append(st.pop())

            st.append(p)

    while st:
        result.append(st.pop())

    for r in result:
        if r == '+':
            num1 = st.pop()
            num2 = st.pop()
            st.append(num2 + num1)

        elif r == '*':
            num1 = st.pop()
            num2 = st.pop()
            st.append(num2 * num1)

        else:
            st.append(r)

    return st.pop()


for tc in range(1, 11):
    N = int(input())
    string = input()

    ans = calculator(string)
    print(f'#{tc} {ans}')
