def stars(num):
    star = '*'

    for i in range(num):
        print(star * (i+1))
    
number = int(input())
stars(number)