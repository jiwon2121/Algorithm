import sys
sys.stdin = open('./sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    bin_num = list(input())
    tri_num = list(input())

    bin_set = set()
    tri_set = set()

    for i in range(len(bin_num)):
        btoi = 0
        for b in range(len(bin_num)):
            if b == i:
                btoi += ((int(bin_num[-1 - b]) + 1) % 2) * (2 ** b)
            else:
                btoi += int(bin_num[-1 - b]) * (2 ** b)

        bin_set.add(btoi)

    for j in range(len(tri_num)):
        ttoi = [0, 0]
        lst = [0, 1, 2]
        for t in range(len(tri_num)):
            if t == j:
                num = int(tri_num[-1 - t])
                lst.pop(num)

                for idx, l in enumerate(lst):
                    ttoi[idx] += l * (3 ** t)

            else:
                ttoi[0] += int(tri_num[-1 - t]) * (3 ** t)
                ttoi[1] += int(tri_num[-1 - t]) * (3 ** t)

        tri_set.update(ttoi)

    inter = bin_set & tri_set
    print(f'#{tc} {inter.pop()}')