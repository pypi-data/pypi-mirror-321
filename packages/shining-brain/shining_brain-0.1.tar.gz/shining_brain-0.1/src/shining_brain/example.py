import string
from shining_brain.util import load_file_into_database, generate_ddl, generate_column_mapping
from shining_brain.logger_setup import setup_logger

logger = setup_logger('main.py')


def refresh_data(filename, table_name):
    filepath = f"/Users/thomas/Documents/english-language/{filename}.csv"
    logger.info('\n \n%s\n', generate_ddl(filepath, table_name))
    column_mapping = generate_column_mapping(filepath)
    before_statement = f'delete from {table_name} where id > 0'
    load_file_into_database(filepath, table_name, column_mapping, before_statement)


def print_rangoli(size):
    width = 4 * size - 3
    letters = string.ascii_lowercase[:size]
    for i in range(size - 1, -1, -1):
        if i == size - 1:
            print(letters[i].center(width, '-'))
        else:
            s = []
            for j in range(0 + i, size):
                s.append(letters[j])
            s1 = s[::-1][:len(s) - 1]
            s1.extend(s)
            print('-'.join(s1).center(width, '-'))
    for i in range(1, size):
        if i == size - 1:
            print(letters[i].center(width, '-'))
        else:
            s = []
            for j in range(i, size):
                s.append(letters[j])
            s1 = s[::-1][:len(s) - 1]
            s1.extend(s)
            print('-'.join(s1).center(width, '-'))


if __name__ == '__main__':
    refresh_data('wordbank', 'word_bank')
    refresh_data('transactions', 'transaction')
    # print_rangoli(3)
    # print_rangoli(5)
    # print_rangoli(10)
