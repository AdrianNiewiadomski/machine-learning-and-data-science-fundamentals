import math
import matplotlib.pyplot as pl


def read_data():
    time = []
    time_series = []

    with open('data/simple_fourier_transform_data.txt', 'r') as file:
        for line in file:
            data = line.replace('\n', '').split('	')
            time.append(int(data[0]))
            time_series.append(float(data[1]))

    return time, time_series


def calculate_fourier_transform_for_given_frequency(time, time_series, frequency):
    cos_sum = 0
    sum_sin = 0

    for i in range(len(time)):
        cos_sum += math.cos(time[i] * 2 * math.pi / frequency) * time_series[i]
        sum_sin += math.sin(time[i] * 2 * math.pi / frequency) * time_series[i]

    return cos_sum, sum_sin


def calculate_fourier_transform(time, time_series):
    cos = []
    sin = []

    for frequency in range(len(time)):
        c, s = calculate_fourier_transform_for_given_frequency(time, time_series, frequency +1 )
        cos.append(c)
        sin.append(s)

    return cos, sin


def find_max_of_list(some_list):
    max_i = -math.inf
    max_el = -math.inf
    for i, list_element in enumerate(some_list):
        if list_element > max_el:
            max_el = list_element
            max_i = i
    return max_i


def main():
    time, time_series = read_data()
    print(time)
    print(time_series)

    pl.plot(time, time_series)
    pl.show()

    cos, sin = calculate_fourier_transform(time, time_series)
    pl.plot(range(len(time)), cos, range(len(time)), sin, 'r--')
    pl.show()

    max_cos = find_max_of_list(cos)
    max_sin = find_max_of_list(sin)
    print('The frequency of your time series is :', max(max_cos, max_sin))


if __name__ == '__main__':
    main()
