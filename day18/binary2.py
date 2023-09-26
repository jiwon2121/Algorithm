import sys
sys.stdin = open('./5186_input.txt')

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    if num == 0:
        print(f'{tc} 0')

    else:
        result = []
        i = 1
        add = 0
        while i < 13:
            if num >= add + 2 ** (-i):
                add += 2 ** (-i)
                result.append(1)
            else:
                result.append(0)

            if num == add:
                result = list(map(str, result))
                result = ''.join(result).rstrip('0')
                break

            i += 1

        else:
            result = 'overflow'

        print(f'#{tc} {result}')