from sympy import *

a, b = 1.4, 2.6
h = round((b - a) / 20, 3)
I = lambda y0, y20, y_sum: h * (((y0 + y20) / 2) + y_sum)
y = lambda x: 1 / sqrt(1.5*x ** 2 +0.7)
x = lambda i: a + i * h
y_arr = [y(x(i)) for i in range(21)]
print('%-3s %-7s %-s' % ('i', 'xi', 'yi'))
for i in range(len(y_arr)):
    print('%-3d %-7.3f %-.4f' % (i, x(i), y_arr[i]))
def get_sum(y_arr):
    sum = 0
    for i in range(len(y_arr)):
        if i != 0 and i != 20:
            sum += y_arr[i]
    return round(sum, 4)
print('\nI = %.5f\n' % I(y_arr[0], y_arr[20], get_sum(y_arr)))