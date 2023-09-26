import sys

def dist(d, a, b, f):
    r_speed = a + b
    time = d/r_speed

    return f * time




sys.stdin = open('./s_input.txt')

T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    result = dist(D, A, B, F)

    print(f'#{tc} {result}')

