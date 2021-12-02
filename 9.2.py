print("Введите числа через пробел")
total = 0
while True:
    userintput = input().split(' ')
    try:
        total += sum(map(int, userintput))
        print("Результат: ",total)
    except ValueError:
        break