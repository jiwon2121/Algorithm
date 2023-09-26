import sys
sys.stdin = open('./input1.txt')

T = int(input())
for tc in range(1, T+1):
    bi_num = ''
    for h in list(input()):
        b = bin(int('0x' + h, 16))[2:]
        bi_num += f'{b:>04}'

    l = len(bi_num)
    quot = l // 7
    remain = l % 7

    print(f'#{tc}', end = '')
    for i in range(quot):
        num = int('0b' + bi_num[i * 7:i * 7 + 7], 2)
        print(f' {num}', end = '')

    if remain != 0:
        num = int('0b' + bi_num[quot*7:], 2)
        print(f' {num}')