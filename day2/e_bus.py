import sys

def e_bus(k, n, m_lst):
    stop = 0
    count = 0
    copied_lst = m_lst[:]
    copied_lst.append(n)

    while stop != n:
        can_stop = [x for x in copied_lst if stop < x <= stop + k]

        if can_stop:
            stop = can_stop[-1]
            count += 1

        else:
            return 0

    return count - 1


sys.stdin = open('./4831_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))

    result = e_bus(K, N, M_lst)

    print(f'#{tc} {result}')