import sys

def e_bus(k, n, m_lst):
    stop = 1
    count = 0
    charger = 0
    next_stop = stop

    for m in m_lst:
        charger += 1 << m

    charger += 1 << n

    while stop != 1 << n:
        next_stop = next_stop << k

        while not (charger & next_stop):
            next_stop = next_stop >> 1

            if next_stop == stop:
                return 0

        stop = next_stop
        count += 1

    return count - 1


sys.stdin = open('./4831_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))

    result = e_bus(K, N, M_lst)

    print(f'#{tc} {result}')