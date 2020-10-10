import pandas as pd


def main():
    print('Let\'s say that I have a following data')
    my_data = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
        [41, 42, 43]
    ]
    print('my_data: ', my_data)
    row_names = ['A', 'B', 'C', 'D']
    print('row_names: ', row_names)
    column_names = ['X', 'Y', 'Z']
    print('column_names: ', column_names)

    print('\nI may create a pandas DataFrame object.')
    my_data_frame = pd.DataFrame(
        data=my_data,
        index=row_names,
        columns=column_names)
    print('my_data_frame:')
    print(my_data_frame)

    print('\nNow I can access a column of DataFrame with my_data_frame[\'X\']:')
    print(my_data_frame['X'])

    print('\nor a row with either my_data.loc[\'A\']: ')
    print(my_data_frame.loc['A'])

    print('\nor my_data.iloc[0]: ')
    print(my_data_frame.iloc[0])

    print('\nThe iloc function accepts lists as arguments my_data.iloc[[0, 1]]: ')
    print(my_data_frame.iloc[[0, 1]])

    print('\nIt also supports slicing my_data.iloc[:2]: ')
    print(my_data_frame.iloc[:2])

    print('You may access single elements by either my_data_frame[\'Y\'][\'B\']:')
    print(my_data_frame['Y']['B'])

    print('or with my_data_frame.loc[\'B\'][\'Y\']:')
    print(my_data_frame.loc['B']['Y'])


if __name__ == '__main__':
    main()
