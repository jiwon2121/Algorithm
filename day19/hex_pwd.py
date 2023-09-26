import sys
sys.stdin = open('./input2.txt')

pwd_dict = {
    '001101' : 0,
    '010011' : 1,
    '111011' : 2,
    '110001' : 3,
    '100011' : 4,
    '110111' : 5,
    '001011' : 6,
    '111101' : 7,
    '011001' : 8,
    '101111' : 9
}

T = int(input())
for tc in range(1, T+1):
    bi_num = ''
    for h in list(input().strip()):
        b = bin(int('0x' + h, 16))[2:]
        bi_num += f'{b:>04}'

    l = len(bi_num)
    i = 0
    result = []
    while l - i >= 6:
        if bi_num[l-i-1] == '1':
            code = bi_num[l - i - 6 : l - i]
            pwd = pwd_dict[code]
            result.append(pwd)
            i += 6
        else:
            i += 1

    print(f'#{tc}', *result[::-1])