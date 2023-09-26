import sys
sys.stdin = open('./input1.txt')

def calculator(problem):
    result = []
    st = []

    for p in problem:
        if p == '+':
            if not st:
                st.append(p)

            else:
                while len(st) >= 1:
                    result.append(st.pop())
                st.append(p)

        else:
            result.append(p)

    while len(st) > 0:
        result.append(st.pop())


    for r in result:
        if r == '+':
            pop1 = int(st.pop())
            pop2 = int(st.pop())
            st.append(pop2 + pop1)

        else:
            st.append(r)

    return st.pop()



for tc in range(1, 11):
    N = int(input())
    string = input()

    ans = calculator(string)

    print(f'#{tc} {ans}')