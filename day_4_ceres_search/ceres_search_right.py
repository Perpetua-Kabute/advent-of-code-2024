
def get_content():
    with open("input.txt", "r") as f:
        word_matrix = []
        lines = f.read().splitlines()
        for line in lines:
            line.rstrip('\n')
            row = [x for x in line]
            word_matrix.append(row)
    return word_matrix

def search_horizontal_forward(input_matrix):
    number_of_words = 0
    for j in range(len(input_matrix)):
        for i in range(len(input_matrix[j]) - 3):
            row = input_matrix[j]
            if row[i] == "X" and row[i+1] == "M" and row[i+2] == "A" and row [i+3] == "S":
                number_of_words += 1
    return number_of_words


def check_index_out_of_bound():
    pass

def search_horizontal_backward(input_matrix):
    number_of_words = 0
    for j in range(len(input_matrix)):
        for i in range(3, len(input_matrix[j])):
            row = input_matrix[j]
            if row[i] == "X" and row[i-1] == "M" and row[i-2] == "A" and row[i-3] == "S":
                number_of_words += 1
    return number_of_words

def search_vertical_upward(input_matrix):
    number_of_words = 0
    for j in range(3, len(input_matrix)):
        for i in range(len(input_matrix[j])):
            row = input_matrix[j]
            if row[i] == "X" and input_matrix[j-1][i] == "M" and input_matrix[j-2][i] == "A" and input_matrix[j-3][i] == "S":
                number_of_words += 1
    return number_of_words

def search_vertical_downward(input_matrix):
    xmas_words = 0
    for j in range(len(input_matrix) - 3):
        for i in range(len(input_matrix[j])):
            if input_matrix[j][i] == "X" and input_matrix[j+1][i] == "M" and input_matrix[j+2][i] == "A" and input_matrix[j+3][i] == "S":
                xmas_words += 1
    # print(xmas_words)
    return xmas_words

def search_pos_diagonal_forward(input_matrix):
    number_of_words = 0
    for j in range(len(input_matrix) - 3):
        for i in range(len(input_matrix[j]) - 3):
            if input_matrix[j][i] == "X" and input_matrix[j+1][i+1] == "M" and input_matrix[j+2][i+2] == "A" and input_matrix[j+3][i+3] == "S":
                number_of_words += 1
    # for j in range(1, len(input_matrix) - 3):
    #     for i in range(j):
    #         if input_matrix[j][i] == "X" and input_matrix[j+1][i+1] == "M" and input_matrix[j+2][i+2] == "A" and input_matrix[j+3][i+3] == "S":
    #             number_of_words += 1
    return number_of_words
def search_pos_diagonal_backward(input_matrix):
    number_of_words = 0
    for j in range(3, len(input_matrix)):
        for i in range(3, len(input_matrix[j])):
            if input_matrix[j][i] == "X" and input_matrix[j-1][i-1] == "M" and input_matrix[j-2][i-2] == "A" and input_matrix[j-3][i-3] == "S":
                number_of_words += 1
    return number_of_words
    
def search_neg_diagonal_forward(input_matrix):
    number_of_words = 0
    for j in range(3, len(input_matrix)):
        for i in range(len(input_matrix[j]) - 3):
            if input_matrix[j][i] == "X" and input_matrix[j-1][i+1] == "M" and input_matrix[j-2][i+2] == "A" and input_matrix[j-3][i+3] == "S":
                number_of_words += 1
    return number_of_words

def search_neg_diagonal_backward(input_matrix):
    number_of_words = 0
    for j in range(len(input_matrix) -3):
        for i in range(3, len(input_matrix[j])):
            if input_matrix[j][i] == "X" and input_matrix[j+1][i-1] == "M" and input_matrix[j+2][i-2] == "A" and input_matrix[j+3][i-3] == "S":
                number_of_words += 1
    return number_of_words

def find_total_number_of_words(input_matrix):
    return search_horizontal_forward(input_matrix) + search_horizontal_backward(input_matrix) + search_vertical_upward(input_matrix) + search_vertical_downward(input_matrix) + search_pos_diagonal_forward(input_matrix) + search_pos_diagonal_backward(input_matrix) + search_neg_diagonal_forward(input_matrix) + search_neg_diagonal_backward(input_matrix)

print(find_total_number_of_words(get_content()))