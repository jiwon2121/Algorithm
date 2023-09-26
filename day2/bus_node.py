import sys

def bus_node(start_lst, end_lst):
    bus_stop = [0 for _ in range(5001)]

    for start, end in zip(start_lst, end_lst):
        for i in range(start, end + 1):
            bus_stop[i] += 1

    return bus_stop


sys.stdin = open('./s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = [0]
    B = [0]
    C = []

    for _ in range(N):
        a,b = list(map(int, input().split()))
        A.append(a)
        B.append(b)

    P = int(input())
    for _ in range(P):
        c = int(input())
        C.append(c)

    result = bus_node(A, B)

    print(f'#{tc}', end = '')
    for i in C:
        print(f' {result[i]}', end = '')

    print()
