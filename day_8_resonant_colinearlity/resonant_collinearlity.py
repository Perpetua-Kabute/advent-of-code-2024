import re
def get_content():
    antenna_map = []
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            row = list(line)
            antenna_map.append(row)
    
    print(antenna_map[2:3])
    return antenna_map

def get_antinode_positions(antenna1, antenna2, rows, cols):
    a_x, a_y = antenna1
    b_x, b_y = antenna2
    diff_x, diff_y = (b_x - a_x),(b_y - a_y)

    antenna_positions = {antenna1, antenna2}
    position_top = (a_x - diff_x),(a_y - diff_y)
    if 0 <= position_top[0] < rows and 0 <= position_top[1] < cols:
            antenna_positions.add(position_top)

    position_bottom = (b_x + diff_x),(b_y + diff_y)
    if 0 <= position_bottom[0] < rows and 0<= position_bottom[1] < cols:
            antenna_positions.add(position_bottom)
    
    while 0 <= position_bottom[0] < rows and 0<= position_bottom[1] < cols:
        b_x,b_y = position_bottom
        position_bottom = (b_x + diff_x),(b_y + diff_y)
        if 0 <= position_bottom[0] < rows and 0<= position_bottom[1] < cols:
            antenna_positions.add(position_bottom)
        # print(f" antenna positions  bottom = {antenna_positions}")

    while 0 <= position_top[0] < rows and 0 <= position_top[1] < cols:
        a_x, a_y = position_top
        position_top = (a_x - diff_x),(a_y - diff_y)
        if 0 <= position_top[0] < rows and 0 <= position_top[1] < cols:
            antenna_positions.add(position_top)
        # print(f" antenna positions top= {antenna_positions}")
    # print(f" antenna positions = {antenna_positions}")
    return antenna_positions

def find_all_antenna_postions(input):
    antenna_positions = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if (re.match("[A-Za-z\d]", input[r][c])) != None:
                antenna1_pos = (r,c)
                print(f" pos 1 = {r,c}")
                for r_1 in range(r, len(input)):
                    for c_1 in range(len(input[r_1])):
                        if input[r_1][c_1] == input[r][c] and (r,c) != (r_1,c_1):
                            antenna2_pos = (r_1,c_1)
                            print(f"pos 2 = {r_1,c_1}")
                            antenna_positions.update(get_antinode_positions(antenna1 = antenna1_pos, antenna2= antenna2_pos, rows = len(input), cols = len(input[r])))
                            print(f"Antenna position = {antenna_positions}")
                            break
                    
    print(antenna_positions)
    return antenna_positions

if __name__ == "__main__":
    input = get_content()
    print(len(find_all_antenna_postions(input)))