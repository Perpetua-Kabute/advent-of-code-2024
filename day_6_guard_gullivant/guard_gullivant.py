from guard_direction import GuardDirection
def get_content():
    map = []
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            map.append(list(line))
    return map

def change_direction(current_direction):
    if current_direction == GuardDirection.FORWARD:
        return GuardDirection.DOWNWARD
    elif current_direction == GuardDirection.DOWNWARD:
        return GuardDirection.BACKWARD
    elif current_direction == GuardDirection.BACKWARD:
        return GuardDirection.UPWARD
    else:
        return GuardDirection.FORWARD
def get_current_position(map):
    for row in map:
        for column in row:
            if column == "^":
                return map.index(row), row.index(column)

def walk_upward(current_position, map):
    """I want to return the number of steps the guard walked upward until they found an obstacle"""
    crow, ccolumn = current_position
    positions_visitied = set()
    should_stop = True
    for i in range(crow, 0, -1) :
        """to move upwards...i check the item above...if it is not a # i continue moving"""
        if map[i-1][ccolumn] != "#":
            crow -= 1
            positions_visitied.add((crow, ccolumn))
        else:
            should_stop = False
            positions_visitied.add((crow,ccolumn))
            return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.UPWARD), should_stop

    positions_visitied.add((crow,ccolumn))
    return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.UPWARD), should_stop

def walk_forward(current_position, map):
    crow, ccolumn = current_position
    positions_visitied = set()
    row = map[crow]
    should_stop = True
    for c in range(ccolumn, len(row) -1):
        if row[c+1] == '#':
            should_stop = False
            positions_visitied.add((crow,ccolumn))
            return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.FORWARD), should_stop
        else:
            ccolumn += 1
            positions_visitied.add((crow, ccolumn))
  
    positions_visitied.add((crow,ccolumn))
    return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.FORWARD), should_stop 

def walk_downward(current_position, map):
    crow, ccolumn = current_position
    positions_visitied = set()
    should_stop = True
    for r in range(crow, len(map) - 1):
        if map[r+1][ccolumn] != "#":
            crow += 1
            positions_visitied.add((crow, ccolumn))
        else:
            should_stop = False
            positions_visitied.add((crow,ccolumn))
            return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.DOWNWARD), should_stop
    
    positions_visitied.add((crow,ccolumn))
    return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.DOWNWARD), should_stop

def walk_backward(current_position, map):
    crow, ccolumn = current_position
    positions_visitied = set()
    row = map[crow]
    should_stop = True
    for c in range(ccolumn, 0, -1):
        if row[c-1] == '#':
            should_stop = False
            positions_visitied.add((crow,ccolumn))
            return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.BACKWARD), should_stop
        else:
            ccolumn -= 1
            positions_visitied.add((crow, ccolumn))
    
    positions_visitied.add((crow,ccolumn))
    return positions_visitied, (crow, ccolumn), change_direction(GuardDirection.BACKWARD), should_stop

def move():
    pass
def get_total_positions(input):
    """17"""
    current_position = get_current_position(input)
    positions_covered = {current_position}
    current_direction = GuardDirection.UPWARD
    is_in_a_loop = False
    should_sstop = False
    max_steps = len(input) * len(input[0])
    steps = 0
    while not should_sstop:
        positions, current_position, current_direction, should_sstop= walk_upward(current_position, input)
        steps += len(positions)
        positions_covered.update(positions)
        if not should_sstop:
            positions, current_position, current_direction, should_sstop= walk_forward(current_position, input)
            steps += len(positions)
            positions_covered.update(positions)
            if not should_sstop:
                positions, current_position, current_direction, should_sstop= walk_downward(current_position, input)
                steps += len(positions)
                positions_covered.update(positions)
                if not should_sstop:
                    positions, current_position, current_direction, should_sstop= walk_backward(current_position, input)
                    steps += len(positions)
                    positions_covered.update(positions)
        # steps = len(positions_covered)
        if steps > max_steps :
            is_in_a_loop = True
            should_sstop = True
    return is_in_a_loop, positions_covered

def try_adding_obstacles_per_position(input):
    """
    try adding an obstacle per position then check if the guard is in a loop.
    inelegang and worst time complexity but I've been stuck here for too long...let's move on...might come back later with something better...maybe..maybe not"""
    start_x, start_y = get_current_position(input)
    new_obstacle_points_count = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if (r,c) != (start_x, start_y) and input[r][c] != '#':
                input[r][c] = "#"
                is_in_a_loop, positions_passed = get_total_positions(input)
                if is_in_a_loop:
                    new_obstacle_points_count += 1
                input[r][c] = "."
                 
    return new_obstacle_points_count  

    
             
def try_to_put_obstacles(input):
    """6"""
    current_position = get_current_position(input)
    positions_covered = {current_position}
    obstacle_positions = set()
    current_direction = GuardDirection.UPWARD
    should_sstop = False
    while not should_sstop:
        obstacle_positions.add(check_obstacle_passed_in_turning_drection(current_position=current_position, current_direction=current_direction,positions_passed=positions_covered,map=input))
        positions, current_position, current_direction, should_sstop= walk_upward(current_position, input)
        positions_covered.update(positions)
        if not should_sstop:
            obstacle_positions.add(check_obstacle_passed_in_turning_drection(current_position=current_position, current_direction=current_direction,positions_passed=positions_covered,map=input))
            positions, current_position, current_direction, should_sstop= walk_forward(current_position, input)
            positions_covered.update(positions)
            if not should_sstop:
                obstacle_positions.add(check_obstacle_passed_in_turning_drection(current_position=current_position, current_direction=current_direction,positions_passed=positions_covered,map=input))
                positions, current_position, current_direction, should_sstop= walk_downward(current_position, input)
                positions_covered.update(positions)
                if not should_sstop:
                    obstacle_positions.add(check_obstacle_passed_in_turning_drection(current_position=current_position, current_direction=current_direction,positions_passed=positions_covered,map=input))
                    positions, current_position, current_direction, should_sstop= walk_backward(current_position, input)
                    positions_covered.update(positions)
    print(positions_covered)
    return obstacle_positions

def check_obstacle_passed_in_turning_drection(current_position, current_direction, positions_passed, map):
    """return obstacle if it is there and has been passed before"""
    crow, ccolumn = current_position

    if current_direction == GuardDirection.UPWARD: #this guy is currently moving upward
            for i in range(crow, 0, -1) :
                if map[i-1][ccolumn] != "#":
                    row = map[crow]
                    if (i, ccolumn) in positions_passed:
                        for c in range(ccolumn, len(row) -1):
                            if row[c+1] == '#':
                                if (i,c) != (crow,ccolumn):
                                    return(crow -1,ccolumn)
                    crow -= 1

    elif current_direction == GuardDirection.FORWARD: #this guy is currently moving forward
        for c in range(ccolumn, len(map[crow]) -1):
            if map[crow][c+1] != '#':
                if (crow, c) in positions_passed:
                    for r in range(crow, len(map) - 1):
                        if map[r+1][ccolumn] == "#" and (r,c) != (crow, ccolumn):
                            return(crow,ccolumn + 1)
            ccolumn += 1

    elif current_direction == GuardDirection.DOWNWARD: #this guy is currently moving downward and turning backwards
        for r in range(crow, len(map) - 1): 
            if map[r+1][ccolumn] != "#": 
                if(r, ccolumn) in positions_passed:
                    for c in range(ccolumn, 0, -1): 
                        row = map[r]
                        if row[c-1] == '#' and (r,c) != (crow,ccolumn):
                                return(crow + 1, ccolumn )         
                crow += 1

    elif current_direction == GuardDirection.BACKWARD: # this guy is currently moving backward
        for c in range(ccolumn, 0, -1):
            if map[crow][c-1] != '#':
                if(crow, c) in positions_passed:
                    for r in range(crow, 0, -1) :
                        if map[r-1][ccolumn] == "#"and  (r,c) != (crow,ccolumn):
                                return(crow,ccolumn -1)
            ccolumn -= 1

def main():

    map = get_content()
    print(try_adding_obstacles_per_position(map))

if __name__ == "__main__":
    main()