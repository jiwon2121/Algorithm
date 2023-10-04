def stars(num):
    line = ''
    for _ in range(num):
        line += '* '

    for i in range(1, num + 1):
        if i % 2 == 1:
            print(line)

        else:
            print(line[::-1])


number = int(input())
stars(number)
