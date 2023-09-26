import sys
sys.stdin = open('./sample_input2.txt')

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

def find():
        cd = []
        for row in array:
            temp = []
            for ele in row:
                b = bin(int('0x' + ele, 16))[2:]
                temp.append(f'{b:>04}')

            cd.append(''.join(temp).rstrip('0'))

        pwd = []
        for b in cd:
            while b:
                temp = []
                l = len(b)
                count = 1
                for num in ['1','0','1','0']:
                    while b[-1-count] == num:
                        count += 1

                dup = count // 7
                for c in range(8):
                    code = b[l-count*(c+1):l-count*c:dup]
                    temp.append(pwd_dict[code])

                b = b[:l-count*8].rstrip('0')
                if temp and temp not in pwd:
                    pwd.append(temp)

        result = 0
        for nums in pwd:
            total = 0
            total += sum(nums[0:8:2])
            total += sum(nums[1:8:2]) *3

            if total % 10 == 0:
                result += sum(nums[0:8])

        print(result)


T = int(input().strip())
for tc in range(1, T+1):
    N,M = map(int, input().strip().split())
    array = []
    for _ in range(N):
        s = list(input().strip().rstrip('0'))
        if s and s not in array:
            array.append(s)
    print(f'#{tc}', end = ' ')
    find()
