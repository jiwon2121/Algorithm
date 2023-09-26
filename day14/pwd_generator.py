import sys

sys.stdin = open('./input1.txt')

def pwd(arr):
    while True:
        for i in range(1, 6):
            num = array.pop(0)
            num -= i

            if num <= 0:
                num = 0
                array.append(num)
                return

            array.append(num)

for _ in range(10):
    tc = input()
    array = list(map(int, input().split()))
    pwd(array)
    print(f'#{tc}', * array)