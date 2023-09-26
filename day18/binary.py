import sys
sys.stdin = open('./5185_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    print(f'#{tc}', f'{bin(int("0x"+num, 16))[2:]:>0{int(N)*4}}')