import sys
sys.stdin = open('./input3.txt')

for tc in range(1, 11):
    N = int(input())
    array = [input().split() for _ in range(100)]
    count = 0
    for j in range(100):
        flag = True
        for i in range(100):
            ele = array[i][j]

            if flag:
                if ele == '1':
                    flag = False

            else:
                if ele == '2':
                    count += 1
                    flag = True

    print(f'#{tc} {count}')