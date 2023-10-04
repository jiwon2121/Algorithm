def r_stars(num):
    star = '*'
    space = ' '

    for i in range(num):
        space_len = i
        star_len = num - i
        
        print(space * space_len, end = '')
        print(star * star_len)
    
number = int(input())
r_stars(number)