import unittest
from guard_direction import GuardDirection
from guard_gullivant import change_direction
from guard_gullivant import get_current_position
from guard_gullivant import walk_upward
from guard_gullivant import walk_forward
from guard_gullivant import walk_downward
from guard_gullivant import walk_backward
from guard_gullivant import get_total_positions
from guard_gullivant import check_obstacle_passed_in_turning_drection
from guard_gullivant import try_adding_obstacles_per_position

class GuardGullivantTestCase(unittest.TestCase):
    def test_change_direction(self):
        result = change_direction(GuardDirection.BACKWARD)
        expected = GuardDirection.UPWARD
        self.assertEqual(result, expected)
    def test_get_current_position(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        result = get_current_position(input)
        expected = 6,4
        return self.assertEqual(result, expected)
    def test_walk_upwards(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        result = walk_upward((6,4), input)
        expected = {(5,4), (4,4), (3,4), (2,4), (1,4)}, (1,4), GuardDirection.FORWARD, False
        self.assertEqual(result, expected)

    def test_walk_forward(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        result = walk_forward((1,4), input)
        expected = {(1,5), (1,6), (1,7), (1,8)}, (1,8), GuardDirection.DOWNWARD, False
        self.assertEqual(result, expected)

    def test_walk_downward(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        result = walk_downward((7,7), input)
        expected = {(8,7), (9,7)}, (9,7), GuardDirection.BACKWARD, True
        self.assertEqual(result, expected)
    def test_walk_backward(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        result = walk_backward((6,8), input)
        expected = {(6,7), (6,6), (6,5),(6,3), (6,4), (6,2)}, (6,2), GuardDirection.UPWARD, False
        self.assertEqual(result, expected)

    def test_get_total_step(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        result = get_total_positions(input)
        expected = False , {(3, 4),(4, 3),(5, 4),(4, 6),(8, 3),(8, 6),(1, 6),(2, 8),(7, 4),(6, 2),(7, 1),(7, 7),(6, 5),(6, 8),(4, 2),(4, 5),(5, 6),
                            (4, 8),(8, 2),(9, 7),(8, 5),(2, 4),(1, 5),(1, 8),(6, 4),(7, 3),(6, 7),(7, 6),(5, 2),(4, 4),(3, 8),(8, 4),(5, 8),(8, 1),
                            (8, 7),(1, 4),(1, 7),(7, 2),(6, 6),(7, 5),(6, 3)}
        self.assertEqual(result, expected)
    
    def test_add_obstacle_while_going_backward(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        positions_passed= set()
        positions_passed.add((6,4))
        positions_passed.update(walk_upward(current_position=(6,4), map=input)[0])
        positions_passed.update(walk_forward(current_position=(1,4), map=input)[0])
        positions_passed.update(walk_downward(current_position=(1,8), map=input)[0])
        result = check_obstacle_passed_in_turning_drection(current_direction=GuardDirection.BACKWARD, current_position=(6,8), positions_passed=positions_passed, map = input)
        expected = (6,3)
        self.assertEqual(result, expected)
        
    def test_add_obstacle_while_going_downward(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        positions_passed= set()
        positions_passed.add((6,4))
        positions_passed.update(walk_upward(current_position=(6,4), map=input)[0])
        positions_passed.update(walk_forward(current_position=(1,4), map=input)[0])
        positions_passed.update(walk_downward(current_position=(1,8), map=input)[0])
        positions_passed.update(walk_backward(current_position=(6,8), map=input)[0])
        positions_passed.update(walk_upward(current_position=(6,2), map=input)[0])
        positions_passed.update(walk_forward(current_position=(4,2), map=input)[0])
        result = check_obstacle_passed_in_turning_drection(current_direction=GuardDirection.DOWNWARD, current_position=(4,6), positions_passed=positions_passed, map = input)
        expected = (7,6)
        self.assertEqual(result, expected)

    def test_going_forward(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
        positions_passed= set()
        positions_passed.add((6,4))
        positions_passed.update(walk_upward(current_position=(6,4), map=input)[0])
        positions_passed.update(walk_forward(current_position=(1,4), map=input)[0])
        positions_passed.update(walk_downward(current_position=(1,8), map=input)[0])
        positions_passed.update(walk_backward(current_position=(6,8), map=input)[0])
        positions_passed.update(walk_upward(current_position=(6,2), map=input)[0])
        positions_passed.update(walk_forward(current_position=(4,2), map=input)[0])
        positions_passed.update(walk_downward(current_position=(4,6), map=input)[0])
        positions_passed.update(walk_backward(current_position=(8,6), map=input)[0])
        positions_passed.update(walk_upward(current_position=(8,1), map=input)[0])
        result = check_obstacle_passed_in_turning_drection(current_direction=GuardDirection.FORWARD, current_position=(7,1), positions_passed=positions_passed, map = input)
        expected = (7,7)
        self.assertEqual(result, expected)

    # def test_blocking_at_the_end(self):
        # input =  [
        #             ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        #             ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        #             ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        #             ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
        #             ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        #             ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        #             ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
        #             ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
        #             ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        #             ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
        #             ]
        # positions_passed= set()
        # positions_passed.add((6,4))
        # positions_passed.update(walk_upward(current_position=(6,4), map=input)[0])
        # positions_passed.update(walk_forward(current_position=(1,4), map=input)[0])
        # positions_passed.update(walk_downward(current_position=(1,8), map=input)[0])
        # positions_passed.update(walk_backward(current_position=(6,8), map=input)[0])
        # positions_passed.update(walk_upward(current_position=(6,2), map=input)[0])
        # positions_passed.update(walk_forward(current_position=(4,2), map=input)[0])
        # positions_passed.update(walk_downward(current_position=(4,6), map=input)[0])
        # positions_passed.update(walk_backward(current_position=(8,6), map=input)[0])
        # positions_passed.update(walk_upward(current_position=(8,1), map=input)[0])
        # positions_passed.update(walk_forward(current_position=(7,1), map=input)[0])
        # result = check_obstacle_passed_in_turning_drection(current_direction=GuardDirection.DOWNWARD, current_position=(7,7), positions_passed=positions_passed, map = input)
        # expected = (7,9)
        # self.assertEqual(result, expected)
    
    def test_find_all_possible_obstacle_positions(self):
        input =  [
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
                    ]
       
        result = try_adding_obstacles_per_position(input)
        expected = (6)
        self.assertEqual(result, expected)