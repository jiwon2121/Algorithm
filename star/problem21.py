def stars(num):
    lines = ['','']

    for i in range(1, num + 1):
        if i % 2 == 1:
            lines[0] += '* '

        else: 
            lines[1] += ' *'

    for _ in range(num):
        for line in lines:
            if line != '':
                print(line)


number = int(input())
stars(number)