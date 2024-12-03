import re
def fetch_puzzle_input():
    with open("input.txt", "r") as f:
        return f.read()

# def get_valid_mul_instructions(instructions):
#     """param instructions: string - the jumbled comptuer instructions
#     return: list of string, the valid multiplications in the instructions"""

#     return re.findall("mul\(\d{1,3},\d{1,3}\)", instructions)

def get_valid_mul_instructions(instructions):
     
    """param instructions: string - the jumbled comptuer instructions
        return: list of string, the valid multiplications in the instructions"""
    search_result = re.findall("(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))", instructions)
    is_enabled = True
    valid_instructions = []
    for result in search_result:
        if(result == "do()"):
            is_enabled = True
        elif(result == "don't()"):
            is_enabled = False
        else:
            if(is_enabled):
                valid_instructions.append(result)
    return valid_instructions

def get_total_multiplication(valid_instructions):
    """param valid_instructions: list of string, the valid multiplications
    return:int result of adding up or multiplications"""
    total_multiplication = 0

    for instruction in valid_instructions:
        first_num, last_num = re.findall("\d{1,3}", instruction)[0],re.findall("\d{1,3}", instruction)[1]
        total_multiplication += int(first_num) * int(last_num)
    return total_multiplication

valid_instructions = get_valid_mul_instructions(fetch_puzzle_input())
print(get_total_multiplication(valid_instructions))