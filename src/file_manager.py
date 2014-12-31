import sys
import re

def extract_columns(line_cursor, column_indexes, 
                   column_delimiters = ['\t', '\x01']):
    """
    Get columns by indexes.
    Args:
        line_cursor: 
            the iter or array of lines
        column_indexes:
            the column indexes for extract
        column_delimiters:
            the delimiter of column
    Returns:
        return a iter of columns
    """
 
    for line in line_cursor:
        column_array = re.split('|'.join(column_delimiters), line)
        yield [column_array[column_index] for column_index in column_indexes]

def output_columns(columns_cursor, column_delimiter = '\t'):
    """
    Combine the string array into line, and print it to output.
    Can use by generator.
    Args:
        columns_cursor:
            The iterator of the column array.
        column_delimiter:
            The delimiter the split column.
    """
    for columns in columns_cursor:
        yield column_delimiter.join(columns)

def transform_column(line_cursor, column_index, transformer, 
                      column_delimiters = ['\t', '\x01']):
    for line in line_cursor:
        column_array = re.split('|'.join(column_delimiters), line)
        column_array[column_index] = str(transformer(column_array[column_index]))
        yield column_delimiters[0].join(column_array)


if __name__ == "__main__":
#    output_columns(extract_columns(sys.stdin, [0]))
    def trans(s):
        return 'a%04d'%len(s)
    transformer = lambda x: len(x)    
    transformed_lines = transform_column(sys.stdin, 0, transformer)
    transformed_lines = transform_column(transformed_lines, 2, trans)
    for line in transformed_lines:
        print line
