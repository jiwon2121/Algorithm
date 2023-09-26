import sys
sys.stdin = open('./input1.txt')

def scanner(n, m, arr):
    result = []
    pwd_dict = {
        '0001101' : 0,
        '0011001' : 1,
        '0010011' : 2,
        '0111101' : 3,
        '0100011' : 4,
        '0110001' : 5,
        '0101111' : 6,
        '0111011' : 7,
        '0110111' : 8,
        '0001011' : 9
    }
    for row in arr:
        if '1' not in row:
            continue

        for i in range(m - 7 + 1):
            count = 0
            while count < 8:
                start = i + count * 7
                code = row[start:start+7]
                if code not in pwd_dict:
                    result = []
                    break

                result.append(pwd_dict[code])
                count += 1

            else:
                return result

def is_pwd(array):
    even = 0
    odd = 0
    for i in range(8):
        if i % 2 == 0:
            even += array[i]
        else:
            odd += array[i]

    if (even*3 + odd) % 10 == 0:
        return sum(array)

    return 0



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pwd = [input() for _ in range(N)]

    trans = scanner(N, M, pwd)
    ans = is_pwd(trans)
    print(f'#{tc} {ans}')