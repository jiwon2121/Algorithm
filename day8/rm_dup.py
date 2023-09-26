import sys

def rm_dup(words):
    st = []
    point = -1

    for w in words:
        if point == -1 or w != st[point]:
            st.append(w)
            point +=1

        else:
            st.pop()
            point -= 1

    return point + 1




sys.stdin = open('./4873_input.txt')

T = int(input())

for tc in range(1, T + 1):
    words = input()

    ans = rm_dup(words)
    print(f'#{tc} {ans}')