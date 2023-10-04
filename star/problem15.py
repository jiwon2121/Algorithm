def stars(num):
    line_len = num * 2 -1
    for i in range(num):
        if i == 0:
            line = '*'
            print(f'{line:^{line_len}}')
        
        else:
            line = '*' + ' ' * (i * 2 - 1) + '*'
            print(f'{line:^{line_len}}')
    pass


number = int(input())
stars(number)