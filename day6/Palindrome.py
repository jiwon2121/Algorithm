def is_palindrome(word):
    quot = len(word) // 2
    remain = len(word) % 2
    palindrome = word[:quot+remain-1:-1]
    return int(word[:quot] == palindrome)

T = int(input())

for tc in range(1, T + 1):
    word = input()

    print(f'{tc}', is_palindrome(word))