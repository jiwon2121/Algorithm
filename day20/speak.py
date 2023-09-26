import sys
sys.stdin = open('./sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    array = [[] for _ in range(15)]

    for _ in range(5):
        for i, s in enumerate(input()):
            array[i].append(s)

    print(f'#{tc}', end = ' ')
    for arr in array:
        print(*arr, sep='', end='')
    print()