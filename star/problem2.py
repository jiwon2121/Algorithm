def r_stars(num):
    star = '*'
    space = ' '

    for i in range(num):
        star_len = i + 1
        space_len = num - star_len
        
        print(space * space_len, end = '')
        print(star * star_len)


number = int(input())

r_stars(number)