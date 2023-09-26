import sys

def card_max(card_lst):
    card_count = [0 for _ in range(10)]
    max_count = 0
    max_num = 0

    for card in card_lst:
        card_count[card] += 1

    for i, count in enumerate(card_count):
        if count >= max_count:
            max_count = count
            max_num = i

    return (max_num, max_count)


sys.stdin = open('./4834_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    result = card_max(cards)

    print(f'#{tc} {result[0]} {result[1]}')
