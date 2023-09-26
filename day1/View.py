def view(n, t_list):
    result = 0
    for i in range(2, n - 2):
        height = t_list[i]
        diff_max = 255

        for move in [-2, -1, 1, 3]:
            diff = height - t_list[i + move]

            if diff > 0:
                if diff < diff_max:
                    diff_max = diff

            else:
                diff_max = 0
                break

        result += diff_max

    return result


for case in range(10):
    N = int(input())
    tower = list(map(int, input().split()))

    count = view(N, tower)

    print(f'#{case + 1} {count}')
