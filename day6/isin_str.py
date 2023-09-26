def is_in(str1, str2):
    val = False
    for i in range(len(str2) - len(str1) + 1):
        if str2[i : i+len(str1)] == str1:
            val = True

    return int(val)


T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = is_in(str1, str2)

    print(f'#{tc} {result}')