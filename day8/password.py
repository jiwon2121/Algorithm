import sys

def password(pw):
    st = []
    point = -1

    for n in pw:
        if point == -1 or st[point] != n:
            st.append(n)
            point += 1

        else:
            st.pop()
            point -= 1

    return ''.join(st)


sys.stdin = open('./input3.txt')

for tc in range(1, 11):
    N, pw = input().split()

    ans = password(pw)
    print(f'#{tc} {ans}')