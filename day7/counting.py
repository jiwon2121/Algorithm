import sys

def counting(str1, str2):
    element_set = set(str1)
    count_dict = {}
    max_count = 0

    for s in str2:
        count_dict[s] = count_dict.setdefault(s, 0) + 1

    for e in element_set:
        value = count_dict.get(e, 0)

        if max_count < value:
            max_count = value

    return max_count


sys.stdin = open('./4865_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = input()
    M = input()

    result = counting(N, M)

    print(f'#{tc} {result}')
