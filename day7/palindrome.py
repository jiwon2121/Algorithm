import sys

def palindrome(n, arr):
    count = 0
    for i in range(8):
        for j in range(8 - n + 1):
            is_row = True
            is_col = True

            for k in range(n // 2):
                if not (is_row or is_col):
                    break

                front = j + k
                back = j + n - 1 - k

                if arr[i][front] != arr[i][back]:
                    is_row = False

                if arr[front][i] != arr[back][i]:
                    is_col = False

            count += int(is_row)
            count += int(is_col)

    return count


sys.stdin = open('./input1.txt')

for tc in range(1, 11):
    N = int(input())
    array = [input() for _ in range(8)]

    result = palindrome(N, array)
    print(f'#{tc} {result}')