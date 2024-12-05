import re

def get_content():
    with open("input.txt", "r") as f:
        word_matrix = []
        lines = f.read().splitlines()
        for line in lines:
            line.rstrip('\n')
            row = [x for x in line]
            word_matrix.append(row)
    return word_matrix

def find_xmas_horizontally(word_search):
    return len(re.findall("xmas", word_search, re.IGNORECASE)) + len(re.findall("samx", word_search, re.IGNORECASE))

def transform_matrix_to_string(input_matrix):
    new_word_search = ""
    for row in input_matrix:
        for column in row:
            new_word_search += column
        new_word_search += "\n"
    return new_word_search

def transform_matrix_vertical_to_horizontal(input_matrix):
    """
    param: input matrix
    return: int the number of times the words a ppear
     transform the mattrix so that what was vertical becomes horizontal, then use the find horizontal serch """
    input_matrix_transformed = []
    for i in range(len(input_matrix[0])):
        new_array = []
        for j in range(len(input_matrix)):
            new_array.append(input_matrix[j][i])
        
        input_matrix_transformed.append(new_array)
    return input_matrix_transformed

def find_xmas_vertically(input_matrix):
    """
    param: input matrix
    return: int the number of times the words a ppear
     transform the mattrix so that what was vertical becomes horizontal, then use the find horizontal serch """
    input_matrix_transformed = transform_matrix_vertical_to_horizontal(input_matrix)
   
    return find_xmas_horizontally(transform_matrix_to_string(input_matrix_transformed))
            
def transform_matrix_diagonal_to_horizontal(input_matrix):
    """
    param: input matrix
    return: int the number of times the words a ppear
     transform the mattrix so that what was vertical becomes horizontal, then use the find horizontal serch """
    input_matrix_transformed = []
    # top left to bottom right
    for j in range(len(input_matrix)):
        if j == 0:
            for i in range(len(input_matrix[0])):
                new_array = []
                inc = 0
                for row in input_matrix:
                    try:
                        new_array.append(row[i +inc])
                        inc += 1
                    except:
                        break
                input_matrix_transformed.append(new_array)
        else:
            new_array = []
            inc = 0
            for row in input_matrix[j:]:
                try:
                    new_array.append(row[inc])
                    inc += 1
                except:
                    break
            input_matrix_transformed.append(new_array)
        
        # top right to bottom left
    for j in range(len(input_matrix)):
        if j == 0:
            for i in range(len(input_matrix[0])):
                new_array = []
                inc = 0
                for row in input_matrix:
                    try:
                        if(i-inc) < 0:
                            pass
                        else:
                            new_array.append(row[i -inc])
                            print(new_array)
                            inc += 1
                    except:
                        break
                input_matrix_transformed.append(new_array)
        else:
            new_array = []
            inc = 0
            for row in input_matrix[j:]:
                try:
                    new_array.append(row[len(input_matrix[0]) - (inc + 1)])
                    print(new_array)
                    inc += 1
                except:
                    break
            input_matrix_transformed.append(new_array)

    for row in input_matrix_transformed:
        print(row)
    return input_matrix_transformed

def find_xmas_diagonally(input_matrix):
    """
    param: input matrix
    return: int the number of times the words a ppear
     transform the mattrix so that what was vertical becomes horizontal, then use the find horizontal serch """
    input_matrix_transformed = []
    # top left to bottom right
    input_matrix_transformed.extend(transform_matrix_diagonal_to_horizontal(input_matrix))

    # bottom right to top left
    """
    transform matrix vertical to diagonal then use top left to bottom right transformation"""
    # matrix_vert_horizontal = transform_matrix_vertical_to_horizontal(input_matrix)
    # input_matrix_transformed.extend(transform_matrix_diagonal_to_horizontal(matrix_vert_horizontal))      

    return find_xmas_horizontally(transform_matrix_to_string(input_matrix_transformed))
    

def find_xmas_from_word_search(input_matrix):
    """
    param imput_matrix: matrix - the input word search
    return: Int the number of times the string occurs, horizontally, vertically, frontwards, bacwards, upwards, downwards, diagonally, diagonally bacwards
    
    forwards ... xmas
    backwards ... samx

    """
    return find_xmas_horizontally(transform_matrix_to_string(input_matrix)) + find_xmas_vertically(input_matrix) + find_xmas_diagonally(input_matrix)
    
print(find_xmas_from_word_search(get_content()))
print((get_content())[-2])