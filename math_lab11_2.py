from math import cos
a, b = 0.8, 1.2
h = (b - a) / 8
I = lambda y_sum: h / 3 * y_sum
x = lambda i: a + i * h
y = lambda x: cos (x) / (x **2+1)
y_arr = [y(x(i)) for i in range(9)]
print('%-3s %-7s %-s' % ('i', 'xi', 'yi'))
for i in range(len(y_arr)):
    print('%-3d %-7.2f %-.4f' % (i, x(i), y_arr[i]))
def get_sum(y):
    sum = 0
    for i in range(len(y)):
        if i == 0 or i == 8:
            sum += y[i]
        else:
            if i % 2 == 0:
                sum += 2 * y[i]
            else:
                sum += 4 * y[i]
    return sum
print('\nI = %.5f\n' % I(get_sum(y_arr)))

y_arr = [[round(i, 4)] for i in y_arr]
length = len(y_arr)
for j in range(4):
    for i in range(length):
        if i != length - 1:
            y_arr[i] += [round(y_arr[i + 1][-1] - y_arr[i][-1], 4)]
    length -= 1
print('%-3s %-10s %-10s %-10s %-10s %-s' % ('i', 'yi', 'd_yi', 'd^2_yi', 'd^3_yi', 'd^4_yi'))
for i in range(len(y_arr)):
    print('%-3d' % i, end=" ")
    for j in range(len(y_arr[i])):
        print('%-10.4f' % y_arr[i][j], end=" ")
    print()