import pandas as pd


def main():
    my_data_frame = pd.DataFrame(data=[
        ['1/6/2019' , 'East', 'Jones', 'Pencil', 95, 1.99, 189.05],
        ['1/23/2019', 'Central', 'Kivell', 'Binder', 50, 19.99, 999.50],
        ['2/9/2019', 'Central', 'Jardine', 'Pencil', 36, 4.99, 179.64],
        ['2/26/2019', 'Central', 'Gill', 'Pen', 27, 19.99, 539.73],
        ['3/15/2019', 'West', 'Sorvino', 'Pencil', 56, 2.99, 167.44],
        ['4/1/2019', 'East', 'Jones', 'Binder', 60, 4.99, 299.40],
        ['4/18/2019', 'Central', 'Andrews', 'Pencil', 75, 1.99, 149.25]],
        columns=['OrderDate', 'Region', 'Rep', 'Item', 'Units', 'UnitCost', 'Total']
    )

    print('my_data_frame:')
    print(my_data_frame)

    print('\nConditional selection of data in DataFrame (WHERE Region=\'East\')')
    print(my_data_frame[my_data_frame['Region'] == 'East'])

    print('\nConditional selection of data in DataFrame (WHERE Total>200)')
    print(my_data_frame[my_data_frame['Total'] > 200])


if __name__ == '__main__':
    main()