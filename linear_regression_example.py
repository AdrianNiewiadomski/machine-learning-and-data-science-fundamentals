import datetime
import matplotlib.pyplot as pl


def load_data(path):
    x = []
    y = []

    with open(path) as file:
        for line in file:
            data = line.split('	')
            x.append(float(data[0]))
            y.append(float(data[1].replace('\n', '')))

    return x, y


def calculate_coefficients_using_loops(x, y):
    s_x = 0
    s_y = 0
    s_xx = 0
    s_xy = 0
    s_yy = 0

    for i, xi in enumerate(x):
        s_x += xi
        s_y += y[i]
        s_xx += xi * xi
        s_xy += xi * y[i]
        s_yy += y[i] * y[i]

    n = len(x)
    delta = n * s_xx - s_x * s_x

    a = (n * s_xy - s_x * s_y) / delta
    b = (s_xx * s_y - s_x * s_xy) / delta

    return n, s_x, s_y, s_xx, s_xy, s_yy, a, b


def main():
    print('First you have to load the data to your program.')
    x, y = load_data('data/linear_regression_data.txt')

    print('The loaded data in my example are: ')
    print('x: ', x)
    print('y: ', y)

    print('You can now calculate coefficients with the method of your choice.')

    start = datetime.datetime.now()
    n, s_x, s_y, s_xx, s_xy, s_yy, a, b = calculate_coefficients_using_loops(x, y)

    print('The calculation has been done in: ', datetime.datetime.now() - start)

    print('The calculated coefficients are:')
    print('a: ', a)
    print('b: ', b)

    print('Additionally you may calculate coefficient of determination r^2')
    r_2 = (n * s_xy - s_x * s_y) * (n * s_xy - s_x * s_y) / ((n * s_xx - s_x * s_x) * (n * s_yy - s_y * s_y))
    print('r_2: ', r_2)

    estimated_y = [a * xi + b for xi in x]
    pl.plot(x, y, 'rs', x, estimated_y)
    pl.show()




if __name__ == '__main__':
    main()
