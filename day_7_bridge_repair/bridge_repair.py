from itertools import product
def get_content():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        input_equations = {}
        for line in lines:
            key, values = line.split(":")
            values = list(values.strip(" ").split(" "))

            input_equations[int(key)] = values
 
    return input_equations
def make_operation_combinations(operation_num):
    symbols = ['+', '*', '||']
    combination = []
    for combo in product(symbols, repeat=operation_num):
        combination.append(list(combo))  # Or process each combo
        # print(combination)
    return combination

# def make_operation_combinations(operation_num):
#     """param operation_num: Int the number of operations...eg 3
#     return: list of sets, the possible combination"""
#     operations = ['+','*','||']
#     operation_combinations = []
#     operation_combinations = [[operations[0]], [operations[1]], [operations[2]]]
#     for i in range(operation_num - 1):
#         new_operation_comb = []
#         for operation in operation_combinations:
#             new_op = operation[:]
#             new_op.append(operations[0])
#             if new_op not in operation_combinations:
#                 new_operation_comb.append(new_op)
#             new_op = operation[:]
#             new_op.append(operations[1])
#             if new_op not in operation_combinations:
#                 new_operation_comb.append(new_op)
#             new_op = operation[:]
#             new_op.append(operations[2])
#             if new_op not in operation_combinations:
#                 new_operation_comb.append(new_op)
#         operation_combinations = []
#         operation_combinations.extend(new_operation_comb)
#     return operation_combinations

def do_operation(sign, num1, num2):
    if sign == "+":
        return int(num1) + int(num2)
    elif sign == "*":
        return int(num1) * int(num2)
    elif sign == "||":
        return int(f"{num1}{num2}")
    
def check_achieves_test_value(test_value, calibration_equation):
    """param test_value: int - the test anser
    param calibration_equation - the list of numbers """
    achieves_test_result = False
    operation_combinations = make_operation_combinations(len(calibration_equation) - 1)
    for combination in operation_combinations:
        calibration_equation_copy = calibration_equation[:]
        for sign in combination:
            if len(calibration_equation_copy) > 1:
                try:
                    first_result = do_operation(sign, calibration_equation_copy[0], calibration_equation_copy[1] ) 
                    # print(f"{calibration_equation_copy[0]} {sign} { calibration_equation_copy[1]} = {first_result}")
                    calibration_equation_copy[0] = first_result
                    del calibration_equation_copy[1]
                    # print(f"calibration equation {calibration_equation_copy}")
                except IndexError:
                    print(IndexError)
                    break
        # print(f"result = {first_result}")
        if first_result == test_value:
            achieves_test_result = True
            return achieves_test_result
            
    return achieves_test_result

def get_total_for_possible_operations(input):
    """param input - dictionary of the numbers and possible answer
    return dictonary - the valid operations"""
    sum = 0
    for equation in input.items():
        # print(f"{equation}")
        if check_achieves_test_value(equation[0],equation[1]):
            # print(f"{equation} achieves")
            sum += equation[0]
    return sum
if __name__ == "__main__":
    input = get_content()
    print(get_total_for_possible_operations(input=input))