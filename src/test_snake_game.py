from unittest import TestCase
from collections import deque
from snake_game import *
from random import randint

class TestGame(TestCase):
    def test_run(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_update_frame(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_draw_game_state(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_terminate_game(self):
        # arrange

        # act

        # assert
        self.fail()


class TestGameModel(TestCase):
    def test_update_game_state(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_get_game_state(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_draw_board(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_draw_snake(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_draw_fruit(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_print_game_state(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_is_snake_bite_self(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_get_board_dimension(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_get_snake_length(self):
        # arrange

        # act

        # assert
        self.fail()

class TestBoard(TestCase):
    def test_get_dimension(self):
        for i in range(1, 10000):
            board = Board(dimension=i)
            self.assertEqual(board.get_dimension(), i)
            self.assertEqual(board.get_dimension(), board.dimension)

    def test_has_fruit_on_spot(self):
        # arrange
        dimension = 15
        board = Board(dimension=dimension)

        for i in range(1, dimension):
            for j in range(1, dimension):
                board.fruit_location = (-1, -1)
                self.assertEqual(board.has_fruit_on_spot((i, j)), False)
                board.fruit_location = (i, j)
                self.assertEqual(board.has_fruit_on_spot((i, j)), True)

    def test_get_fruit_location(self):
        # arrange
        dimension = 15
        board = Board(dimension=dimension)

        board.fruit_location = (-1, -1)
        self.assertEqual(board.get_fruit_location(), (-1, -1))
        for i in range(1, dimension):
            for j in range(1, dimension):
                board.fruit_location = (i, j)
                self.assertEqual(board.get_fruit_location(), (i, j))

    def test_set_fruit_eaten(self):
        # arrange
        dimension = 15
        board = Board(dimension=dimension)

        for i in range(1, dimension):
            for j in range(1, dimension):
                board.fruit_location = (i, j)
                self.assertEqual(board.get_fruit_location(), (i, j))
                board.set_fruit_eaten()
                self.assertEqual(board.get_fruit_location(), (-1, -1))

    def test_is_fruit_eaten(self):
        # arrange
        dimension = 15
        board = Board(dimension=dimension)

        for i in range(1, dimension):
            for j in range(1, dimension):
                board.fruit_location = (i, j)
                self.assertEqual(board.is_fruit_eaten(), False)
                board.set_fruit_eaten()
                self.assertEqual(board.is_fruit_eaten(), True)

    def test_generate_new_fruit(self):
        """
        Here I will randomly generate snake body
        (which might not be like a snake body at
        all) to test the robustness of the generation
        """
        def random_obstacle_genenration(max_obstacle_count, board_dimension):
            obstacle_table = {}
            obstacle_count = randint(1, max_obstacle_count)
            for i in range(1, obstacle_count):
                j = randint(0, board_dimension-1)
                k = randint(0, board_dimension-1)
                obstacle_table[(j, k)] = 1
            return obstacle_table

        dimension = 50
        board = Board(dimension=dimension)

        for i in range(1, 100):
            obstacles = random_obstacle_genenration(max_obstacle_count=500, board_dimension=dimension)
            for j in range(1, 100):
                board.generate_new_fruit(obstacles)
                self.assertFalse(board.get_fruit_location() in obstacles)
                self.assertNotEqual(board.get_fruit_location(), (-1, -1))


class TestSnake(TestCase):

    def test_initialize_body(self):
        # arrange
        init_body_length = 5
        board_dimension = 15

        # act
        snake = Snake(init_body_length=init_body_length, board_dimension=board_dimension)

        # assert
        self.assertEqual(snake.init_body_length, init_body_length)
        self.assertEqual(snake.board_dimension, board_dimension)
        self.assertEqual(snake.move_direction, (1, 0))
        self.assertEqual(type(snake.body_queue), deque)
        self.assertEqual(type(snake.body_table), dict)

        for i in range(0, init_body_length):
            loc = tuple((i, 0))
            self.assertTrue(loc in snake.body_table)
            self.assertTrue(snake.body_queue[init_body_length - i - 1] == loc)

    def test_set_move_direction_body_length_is_one(self):
        """
        length equal to one -- can set all 4 direction
        """
        def test_case(test_case_name, set_key_sequence, key_to_direction_mapping):
            return {
                'test_case_name': test_case_name,
                'set_key_sequence': set_key_sequence,
                'key_to_direction_mapping': key_to_direction_mapping
            }

        def test_logic(self, test_case_):
            snake = Snake(init_body_length=1, board_dimension=3)
            for key_input in test_case_['set_key_sequence']:
                direction = test_case_['key_to_direction_mapping'][key_input]
                snake.set_move_direction(direction)
                self.assertEqual(snake.move_direction, direction)

        # test cases
        key_to_direction_mapping = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1), 'None': (0, 0)}
        test_cases = [
            test_case('set keys clockwise',
                      ['Up', 'Right', 'Down', 'Left'],
                      key_to_direction_mapping),
            test_case('set keys counter clockwise',
                      ['Up', 'Left', 'Down', 'Right'],
                      key_to_direction_mapping),
            test_case('set opposite keys in sequence',
                      ['Up', 'Down', 'Right', 'Left'],
                      key_to_direction_mapping),
            test_case('set same keys twice',
                      ['Up', 'Up', 'Down', 'Down', 'Right', 'Right', 'Left', 'Left'],
                      key_to_direction_mapping)
        ]

        # arrange
        for tc in test_cases:
            test_logic(self, tc)

    def test_set_move_direction_body_length_more_than_one(self):
        """
        length longer than one -- can only set 3 direction, not neck direction
        """
        def test_case(test_case_name, head, neck_position, all_directions):
            return {
                'test_case_name': test_case_name,
                'head': head,
                'neck_position': neck_position,
                'all_directions': all_directions
            }

        def test_logic(test, test_case_):
            snake = Snake(init_body_length=1, board_dimension=3)
            head_ = test_case_['head']
            neck_ = test_case_['neck_position']
            all_directions_ = test_case_['all_directions']

            snake.body_queue = deque([head_, neck_])
            snake.body_table = {head_: 1, neck_: 1}
            snake.move_direction = (0, 0)

            for direction in all_directions_:
                snake.set_move_direction(direction)
                if snake.is_opposite_direction(direction, snake.get_current_direction()):
                    test.assertNotEqual(direction, snake.move_direction)
                else:
                    test.assertEqual(direction, snake.move_direction)

        # test cases
        shared_all_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        shared_head = (1, 1)
        test_cases = [
            test_case('', shared_head, (0, 1), shared_all_directions),
            test_case('', shared_head, (2, 1), shared_all_directions),
            test_case('', shared_head, (1, 0), shared_all_directions),
            test_case('', shared_head, (1, 2), shared_all_directions)
        ]

        for tc in test_cases:
            test_logic(self, tc)

    def test_get_current_direction(self):

        def test_case(test_case_name, head, neck_position, expected_direction):
            return {
                'test_case_name': test_case_name,
                'head': head,
                'neck_position': neck_position,
                'expected_direction': expected_direction
            }

        def test_logic(test, test_case_):

            # arrange
            snake = Snake(init_body_length=1, board_dimension=3)

            # act and assert
            head = test_case_['head']
            neck = test_case_['neck_position']
            direction = test_case_['expected_direction']
            snake.body_queue = deque([head, neck])
            snake.body_table = {head: 1, neck: 1}
            test.assertEqual(snake.get_current_direction(), direction)

        test_cases = [
            test_case('test get Up direction', (1, 1), (0, 1), (1, 0)),
            test_case('test get Down direction', (1, 1), (2, 1), (-1, 0)),
            test_case('test get Right direction', (1, 1), (1, 0), (0, 1)),
            test_case('test get Left direction', (1, 1), (1, 2), (0, -1))
        ]

        for tc in test_cases:
            test_logic(self, tc)

    def test_get_head_neck_diff(self):
        # arrange
        board_dimension = 3
        snake = Snake(board_dimension=board_dimension)

        def test_case(test_case_name, head, neck, direction):
            return {'test_case_name': test_case_name,
                    'head': head,
                    'neck': neck,
                    'direction': direction}

        def test_logic(test, test_case_):
            test.assertEqual(snake.get_head_neck_diff(test_case_['head'],
                                                      test_case_['neck']),
                                                      test_case_['direction'])

        """        
        the head and neck location here are generated, not real head 
        and neck of the snake because we are just testing head/neck
        difference, there is no need to move the whole snake        
        """

        # test case data
        test_cases = [test_case('head pointing right while crossing boarder', (1, 0), (1, 2), (0, 1)),
                      test_case('head pointing left while crossing boarder', (1, 2), (1, 0), (0, -1)),
                      test_case('head pointing down while crossing boarder', (0, 1), (2, 1), (1, 0)),
                      test_case('head pointing up while crossing boarder', (2, 1), (0, 1), (-1, 0)),
                      test_case('head pointing down while NOT crossing boarder', (1, 1), (0, 1), (1, 0)),
                      test_case('head pointing left while NOT crossing boarder', (1, 1), (1, 2), (0, -1)),
                      test_case('head pointing up while NOT crossing boarder', (1, 1), (2, 1), (-1, 0)),
                      test_case('head pointing right while NOT crossing boarder', (1, 1), (1, 0), (0, 1))]

        # run tests
        for tc in test_cases:
            test_logic(self, tc)

    def test_head_location(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.assertEqual(snake.head_location(), snake.body_queue[0])

    def test_next_step_length_equal_to_one(self):

        def test_case(test_case_name, move_direction, expected_next_step, snake_instance):
            return {
                'test_case_name': test_case_name,
                'move_direction': move_direction,
                'expected_next_step': expected_next_step,
                'snake_instance': snake_instance
            }

        def test_logic(test, test_case_):
            # arrange
            snake = test_case_['snake_instance']

            # act and assert
            snake.set_move_direction(test_case_['move_direction'])
            test.assertEqual(snake.next_step(), test_case_['expected_next_step'])

        # test cases
        test_cases = [test_case('body length 1 at (0, 0); next step after setting to left',
                                (0, -1), (0, 2), Snake(1, 3)),
                      test_case('body length 1 at (0, 0); next step after setting to right',
                                (0, 1), (0, 1), Snake(1, 3)),
                      test_case('body length 1 at (0, 0); next step after setting to up',
                                (-1, 0), (2, 0), Snake(1, 3)),
                      test_case('body length 1 at (0, 0); next step after setting to down',
                                (1, 0),(1, 0) , Snake(1, 3))]

        # run tests
        for tc in test_cases:
            test_logic(self, tc)

    def test_next_step_length_more_than_one(self):

        def test_case(test_case_name, move_direction, expected_next_step, snake_instance):
            return {
                'test_case_name': test_case_name,
                'move_direction': move_direction,
                'expected_next_step': expected_next_step,
                'snake_instance': snake_instance
            }

        def test_logic(test, test_case_):
            # arrange
            snake = test_case_['snake_instance']
            snake.body_queue = deque([(1, 1), (0, 1)])
            snake.body_table = {(1, 1): 1, (0, 1): 1}

            # act and assert
            snake.set_move_direction(test_case_['move_direction'])
            test.assertEqual(snake.next_step(), test_case_['expected_next_step'])

        # test cases
        test_cases = [test_case('body pointing down; can set to move down', (1, 0), (2, 1), Snake(1, 3)),
                      test_case('body pointing UP; can NOT set to move up (still down)', (-1, 0), (2, 1), Snake(1, 3)),
                      test_case('body pointing down; can set to move left', (0, -1), (1, 0), Snake(1, 3)),
                      test_case('body pointing down; can set to move right', (0, 1), (1, 2), Snake(1, 3))]

        # run tests
        for tc in test_cases:
            test_logic(self, tc)

    def test_move(self):

        def test_case(test_case_name,
                      init_body_queue,
                      init_body_table,
                      init_move_direction,
                      hit_fruit,
                      expected_body_queue,
                      expected_body_table,
                      expected_body_length,
                      expected_is_bite_self):
            return {'test_case_name': test_case_name,
                    'init_body_queue': init_body_queue,
                    'init_body_table': init_body_table,
                    'init_move_direction': init_move_direction,
                    'hit_fruit': hit_fruit,
                    'expected_body_queue': expected_body_queue,
                    'expected_body_table': expected_body_table,
                    'expected_body_length': expected_body_length,
                    'expected_is_bite_self': expected_is_bite_self}

        def test_logic(test, test_case_):
            # arrange
            snake = Snake(init_body_length=1, board_dimension=3)
            snake.body_queue = test_case_['init_body_queue']
            snake.body_table = test_case_['init_body_table']
            snake.move_direction = test_case_['init_move_direction']

             # act
            snake.move(hit_fruit=test_case_['hit_fruit'])

            # assert
            test.assertEqual(snake.body_queue, test_case_['expected_body_queue'])
            test.assertEqual(snake.body_table, test_case_['expected_body_table'])
            test.assertEqual(snake.get_body_length(), test_case_['expected_body_length'])
            test.assertEqual(snake.is_bite_self(), test_case_['expected_is_bite_self'])

        test_cases = [
            test_case('test normal move',
                      deque([(1, 1), (0, 1)]),
                      {(1, 1): 1, (0, 1): 1},
                      (1, 0),
                      False,
                      deque([(2, 1), (1, 1)]),
                      {(2, 1): 1, (1, 1): 1},
                      2,
                      False),
            test_case('test hit fruit',
                      deque([(1, 1), (0, 1)]),
                      {(1, 1): 1, (0, 1): 1},
                      (1, 0),
                      True,
                      deque([(2, 1), (1, 1), (0, 1)]),
                      {(2, 1): 1, (1, 1): 1, (0, 1): 1},
                      3,
                      False),
            test_case('test bite self',
                      deque([(1, 1), (0, 1), (0, 0), (1, 0), (2, 0)]),
                      {(1, 1): 1, (0, 1): 1, (0, 0): 1, (1, 0): 1, (2, 0): 1},
                      (0, -1),
                      False,
                      deque([(1, 0), (1, 1), (0, 1), (0, 0), (1, 0)]),
                      {(1, 1): 1, (0, 1): 1, (0, 0): 1, (1, 0): 2},
                      5,
                      True)
        ]

        for tc in test_cases:
            test_logic(self, tc)

    def test_is_bite_self(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.assertEqual(snake.is_bite_self(), max(snake.body_table.values()) > 1)

    def test_get_body_length(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.assertEqual(snake.get_body_length(), len(snake.body_queue))
        self.assertEqual(snake.get_body_length(), len(snake.body_table))


class TestGameView(TestCase):
    def test_draw_square(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.fail()

    def test_draw_game_state(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.fail()


class TestGameController(TestCase):
    def test_set_input(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_get_input(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_clear_input(self):
        # arrange

        # act

        # assert
        self.fail()


