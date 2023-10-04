def height(num):
    if num == 1:
        return 1
    
    return height(num - 1) * 2 + 1


def triangle(num):
    ### 점화식
    if num == 1:
        return '*'
    
    t_height = height(num)
    t_len = t_height * 2 - 1
    result = ''
    small_tri_lst = triangle(num - 1).split('\n')
    small_tri_lst = [x.strip() for x in small_tri_lst]

    ### 홀수
    if num % 2 == 1:
        ### part1
        for i in range(t_height // 2):
            if i == 0:
                line = '*'
                result += f'{line : ^{t_len}}\n'
            
            else:
                line = '*' + ' ' * (i * 2 - 1) + '*'
                result += f'{line : ^{t_len}}\n'

        ### part2
        for i in range(t_height // 2):
            line = '*' + (' ' * i * 2) + small_tri_lst[i] + (' ' * i * 2) + '*'
            result += f'{line : ^{t_len}}\n'

        ### part3
        result += '*' * t_len

    ### 짝수
    else:
        ### part3
        result += '*' * t_len + '\n'

        ### part2
        for i in range(t_height // 2):
            blank_len = (t_height // 2 - 1 -i)
            line = '*' + (' ' * blank_len * 2) + small_tri_lst[i] + (' ' * blank_len * 2) + '*'
            result += f'{line : ^{t_len}}\n'

        ### part1
        for i in range(t_height // 2):
            j = t_height // 2 - 1 - i
            if j == 0:
                line = '*'
                result += f'{line : ^{t_len}}\n'
            
            else:
                line = '*' + ' ' * (j * 2 -1) + '*'
                result += f'{line : ^{t_len}}\n'

    result = result.strip('\n')
    return result


number = int(input())
result = triangle(number)
print(result)