x = []
y = []

with open('data/linear_regression_data.txt') as file:
    for line in file:
        data = line.split('	')
        x.append(float(data[0]))
        y.append(float(data[1].replace('\n', '')))

print(x)
print(y)
