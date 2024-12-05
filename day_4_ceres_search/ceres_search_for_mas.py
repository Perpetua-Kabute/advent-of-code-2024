def get_content():
    with open("input.txt", "r") as f:
        word_matrix = []
        lines = f.read().splitlines()
        for line in lines:
            line.rstrip('\n')
            row = [x for x in line]
            word_matrix.append(row)
    return word_matrix

def find_diagonal_mas(input_matrix):
    number_of_words = 0
    for j in range(1, len(input_matrix) -1):
        for i in range(1, len(input_matrix[j]) - 1):
            if input_matrix[j][i] == "A":
                # look at the first positive diagomal
                if ((input_matrix[j-1][i-1] == "M" and input_matrix[j+1][i+1] == "S") or (input_matrix[j-1][i-1] == "S" and input_matrix[j+1][i+1] == "M")) and ((input_matrix[j-1][i+1] == "M" and input_matrix[j+1][i-1] == "S") or (input_matrix[j-1][i+1] == "S" and input_matrix[j+1][i-1] == "M")):
                    number_of_words += 1
    return number_of_words

print(find_diagonal_mas(get_content()))
