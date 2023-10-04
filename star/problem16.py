def stars(num):
    line_len = num * 2 -1
    
    for i in range(num):
        star_n = i + 1
        line = ''
        
        for j in range(star_n):
            if j != 0:
                line += ' '
            
            line += '*'

        print(f'{line:^{line_len}}')
    pass


number = int(input())
stars(number)