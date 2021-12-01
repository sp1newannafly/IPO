a = {'x':0, 'y':0}
b = {'x':0, 'y':0}
a['x'] = float(input())
a['y'] = float(input())
b['x'] = float(input())
b['y'] = float(input())
suma = {}
mult = {}
suma['x'] = a['x'] + b['x']
suma['y'] = a['y'] + b['y']
mult['x'] = a['x'] * b['x'] - a['y'] * b['y']
mult['y'] = a['y'] * b['x'] + a['x'] * b['y']
print('Сумма:   %.2f+%.2fj' % (suma['x'], suma['y']))
print('Произв.: %.2f+%.2f' % (mult['x'], mult['y']))