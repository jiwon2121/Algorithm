import sys

sys.stdin = open('./4880_input.txt')


def winner(p1, p2):
    if p1 == 1:
        if p2 == 2:
            win = 1

        else:
            win = 0

    elif p1 == 2:
        if p2 == 3:
            win = 1

        else:
            win = 0

    else:
        if p2 == 1:
            win = 1

        else:
            win = 0

    return win


def card_game(n, player=False):
    if not player:
        player = [x for x in range(n)]

    if len(player) == 1:
        return player.pop()

    if len(player) == 2:
        # print(player[0], player[1])
        p1 = cards[player[0]]
        p2 = cards[player[1]]

        return player[winner(p1, p2)]

    half = (len(player) + 1)// 2
    left = card_game(n, player[: half])
    right = card_game(n, player[half:])

    win = card_game(n, [left, right])

    return win


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    ans = card_game(N) + 1

    print(f'#{tc} {ans}')