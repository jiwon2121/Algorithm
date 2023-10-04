def stars(num):
    star = '*'
    space = ' '

    for i in range(num):
        space_len = i

        print(space * space_len, end = '')
        print(star * (num - i), end = '')
        print(star * (num - (i + 1)))


number = int(input())
stars(number)