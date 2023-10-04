def make_x(num):
    count = 1
    interval = 1
    line_len = num * 2 + ((num - 2) * 2 + 1)

    while count > 0:
        if count == 1:
            blank_len = (num - 2) * 2 + 1
            line = '*' * num + ' ' * blank_len + '*' * num
            print(f'{line : ^{line_len}}')

        elif count == num:
            line = '*' + ' ' * (num - 2) + '*' + ' ' * (num - 2) + '*'
            print(f'{line : ^{line_len}}')

        else:
            blank_len = (num - 1 - count) * 2 + 1
            element = '*' + ' ' * (num - 2) + '*'
            line = element + ' ' * blank_len + element
            print(f'{line : ^{line_len}}')

        if count == num:
            interval = -1

        count += interval
 
 
number = int(input())
make_x(number)