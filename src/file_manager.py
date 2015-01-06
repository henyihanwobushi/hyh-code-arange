import sys
import re

def static_value(line_cursor, k_indexes, trans, v_indexes, weigh, 
                 column_delimiters = ['\t', '\x01']):
    '''get a dict from stream by transform and weigh'''
    result_dict = {}
    for line in line_cursor:
        columns = re.split('|'.join(column_delimiters), line)
        k = trans([columns[i] for i in k_indexes])
        v = weigh([columns[i] for i in v_indexes])
        result_dict.setdefault(k, 0)
        result_dict[k] += v



def extract_key_from_line(line, column_indexes, transformers, joint_str="", 
                          column_delimiters = ['\t', '\x01']):
    '''extract columns and transform them then join them'''
    columns = extract_columns_from_line(line, column_indexes, 
                                        column_delimiters)
    return joint_str.join([f(i) for f,i in zip(transformers, columns)])

def extract_columns_from_line(line, column_indexes, 
                              column_delimiters = ['\t', '\x01']):
    column_array = re.split('|'.join(column_delimiters), line)
    return [column_array[column_index] for column_index in column_indexes]

def extract_columns(line_cursor, column_indexes, 
                   column_delimiters = ['\t', '\x01']):
    """Extract columns of by indexes"""
    for line in line_cursor:
        return extract_columns_from_line(line, column_indexes, 
                                         column_delimiters)

def output_columns(columns_cursor, column_delimiter = '\t'):
    """
    Combine the string array into line, and print it to output.
    Can use by generator.
    """
    for columns in columns_cursor:
        yield column_delimiter.join(columns)

def transform_column(line_cursor, column_index, transformer, 
                     column_delimiters = ['\t', '\x01']):
    """Transform the column by the transformer"""
    for line in line_cursor:
        column_array = re.split('|'.join(column_delimiters), line)
        column_array[column_index] = str(transformer(column_array[column_index]))
        yield column_delimiters[0].join(column_array)

def gather_by_id(line_cursor, id_column_index, 
                 column_delimiters = ['\t', '\x01']):
    """Gather columns by id columns"""
    line_to_columns = lambda line: re.split('|'.join(column_delimiters), line)
    first_line = line_cursor.next()
    last_id = line_to_columns(first_line)[id_column_index]
    gathered_lines = [first_line]
    for line in line_cursor:
        column_array = line_to_columns(line)
        if last_id == column_array[id_column_index]:
            gathered_lines.append(line)
        else:
            yield gathered_lines
            gathered_lines = [line]
            last_id = column_array[id_column_index]
    yield gathered_lines

if __name__ == "__main__":
#    output_columns(extract_columns(sys.stdin, [0]))
#    def trans(s):
#        return 'a%04d'%len(s)
#    transformer = lambda x: len(x)    
#    transformed_lines = transform_column(sys.stdin, 0, transformer)
#    transformed_lines = transform_column(transformed_lines, 2, trans)
#    for line in transformed_lines:
#        print line
#    lines_array = gather_by_id(sys.stdin, 1)
#    for lines in lines_array:
#        id_str =  re.split('|'.join(['\t', '\x01']), lines[0])[1]
#        print id_str
#        for line in lines:
#            print '\t' + line[:65]
#    print extract_key_from_line('a\tb\tc', [0,1,2], [lambda x: '_'+str(x)]*3)
    
