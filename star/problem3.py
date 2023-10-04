def stars(num):
    star = '*'

    for i in range(num):
        print(star * (5 - i))
    
number = int(input())
stars(number)