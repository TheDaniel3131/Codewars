def to_csv_text(array):
    return '\n'.join(','.join(str(i) for i in row) for row in array)