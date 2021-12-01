total = 0
while True:
    userintput = input().split(' ')
    try:
        total += sum(map(int, userintput))
        print(total)
    except ValueError:
        break