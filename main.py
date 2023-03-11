
table = [[0, 1],
         [0.2, 1.4],
         [0.4, 1.9],
         [0.6, 2.4]]
x1 = 0
x2 = 0.5
x3 = 1
x4 = 1.5

h = table[1][0] - table[0][0]

length = len(table)
for _ in range(3):
    for i in range(length):
        if i != length - 1:
            table[i] = table[i] + [round(table[i + 1][-1] - table[i][-1], 6)]
    length -= 1

print('%-7s %-9s %-9s %-9s %-s' % ('x', 'y', 'd_y', 'd2_y', 'd3_y'))

for i in range(len(table)):
    for j in range(len(table[i])):
        if j == 0:
            print('%-7.1f' % table[i][j], end=" ")
        else:
            print('%-9.3f' % table[i][j], end=" ")
    print()

def get_x0(x):
    for i in range(len(table)):
        if i != len(table) - 1 and table[i][0] < x < table[i + 1][0]:
            return [table[i][0], i]
        if x < table[0][0]:
            return [table[0][0], 0]
        if x > table[-1][0]:
            return [table[-1][0], -1]

def solve_by_diff_newton(x, x0, d_y, d2_y, d3_y):
    t = (x - x0) / h
    first_d = 1/h * (d_y - 1/2 * d2_y + 1/3 * d3_y)
    second_d = 1/h**  2 * (d2_y - d3_y)
    return [first_d, second_d]


def solve_by_diff_bessel(x, x0, d_y, d2_y1, d2_y, d3_y):
    t = (x - x0) / h
    first_d = 1/h * (d_y + ((2*t - 1) / 2) * ((d2_y1 + d2_y) / 2) + ((3*t**2 - 3*t + 1/2) / 6) * d3_y)
    second_d = 1/h**  2 * (((d2_y1 + d2_y) / 2) + ((2*t - 1) / 2) * d3_y)
    return [first_d, second_d]


def solve_by_diff_stirling(x, x0, d_y1, d_y, d2_y, d3_y2, d3_y1):
    t = (x - x0) / h
    first_d = 1/h * (((d_y1 + d_y) / 2) + t * d2_y + ((3*t**2 - 1) / 6) * ((d3_y2 + d3_y1) / 2))
    second_d = 1/h**  2 * (d2_y + t * ((d3_y2 + d3_y1) / 2))
    return [first_d, second_d]


def solve_by_diff_gauss(x, x0, d_y, d2_y, d3_y):
    t = (x - x0) / h
    first_d = 1/h * (d_y + ((2*t - 1) / 2) * d2_y + ((3*t**2 - 1) / 6) * d3_y)
    second_d = 1/h**  2 * (d2_y + t * d3_y)
    return [first_d, second_d]


y = [[0, 0] for i in range(4)]

#x0, i = get_x0(x1)
#y[0][0], y[0][1] = solve_by_diff_newton(x1, x0, table[i][2], table[i][3], table[i][4])

#x0, i = get_x0(x2)
#y[1][0], y[1][1] = solve_by_diff_bessel(x2, x0, table[i][2], table[i-1][3], table[i][3], table[i-1][4])

#x0, i = get_x0(x3)
#y[2][0], y[2][1] = solve_by_diff_stirling(x3, x0, table[i-1][2], table[i][2], table[i-1][3], table[i-2][4], table[i-1][4])

x0, i = get_x0(x1)
y[0][0], y[0][1] = solve_by_diff_gauss(x1, x0, table[i][2], table[i-1][3], table[i-1][4])

x = [x1, x2, x3, x4]

print('\n%-7s %-8s %-s' % ('x', "y'(x)", 'y"(x)'))
for i in range(4):
    print('%-7.2f %-8.3f % -.3f' % (x[i], y[i][0], y[i][1]))