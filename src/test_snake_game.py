from unittest import TestCase
from collections import deque
from snake_game import *


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
        # arrange

        # act

        # assert
        self.fail()

    def test_has_fruit_on_spot(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_get_fruit_location(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_set_fruit_eaten(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_is_fruit_eaten(self):
        # arrange

        # act

        # assert
        self.fail()

    def test_generate_new_fruit(self):
        # arrange

        # act

        # assert
        self.fail()

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

    def test_set_move_direction(self):
        """
        length equal to one -- can set all 4 direction
        """
        # arrange
        snake = Snake(init_body_length=1, board_dimension=3)
        key_to_tuple = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1), 'None': (0, 0)}
        clockwise_keys = ['Up', 'Right', 'Down', 'Left']
        counter_clockwise_keys = ['Up', 'Left', 'Down', 'Right']
        opposite_keys = ['Up', 'Down', 'Right', 'Left']
        same_keys = ['Up', 'Up', 'Down', 'Down', 'Right', 'Right', 'Left', 'Left']
        all_key_arrangements = [clockwise_keys, counter_clockwise_keys, opposite_keys, same_keys]

        # act and assert
        for key_arrangement in all_key_arrangements:
            for key_input in key_arrangement:
                direction = key_to_tuple[key_input]
                snake.set_move_direction(direction)
                self.assertEqual(snake.move_direction, direction)

        """
        length longer than one -- can only set 3 direction, not neck direction
        """
        # arrange
        snake = Snake(init_body_length=1, board_dimension=3)
        direction_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neck_position_list = [(0, 1), (2, 1), (1, 0), (1, 2)]
        head = (1, 1)

        # act and assert
        for neck in neck_position_list:
            snake.body_queue = deque([head, neck])
            snake.body_table = {head: 1, neck: 1}
            snake.move_direction = (0, 0)

            for direction in direction_list:
                snake.set_move_direction(direction)
                if snake.is_opposite_direction(direction, snake.get_current_direction()):
                    self.assertNotEqual(direction, snake.move_direction)
                else:
                    self.assertEqual(direction, snake.move_direction)

    def test_get_current_direction(self):
        # arrange
        snake = Snake(init_body_length=1, board_dimension=3)

        # correct direction with corresponding neck position when head position is (1, 1)
        direction_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neck_position_list = [(0, 1), (2, 1), (1, 0), (1, 2)]
        head = (1, 1)

        # act and assert
        for i in range(len(neck_position_list)):
            neck = neck_position_list[i]
            direction = direction_list[i]
            snake.body_queue = deque([head, neck])
            snake.body_table = {head: 1, neck: 1}
            self.assertEqual(snake.get_current_direction(), direction)

    def test_get_head_neck_diff(self):
        # arrange
        board_dimension = 3
        snake = Snake(board_dimension=board_dimension)

        # act and assert
        """        
        the head and neck location here are generated, not real head 
        and neck of the snake because we are just testing head/neck
        difference, there is no need to move the whole snake        
        """

        head_neck_list_cross_edge = [[(1, 0), (1, 2), (0, 1)],
                                     [(1, 2), (1, 0), (0, -1)],
                                     [(0, 1), (2, 1), (1, 0)],
                                     [(2, 1), (0, 1), (-1, 0)]]

        head_neck_list_not_cross_edge = [[(1, 1), (0, 1), (1, 0)],
                                     [(1, 1), (1, 2), (0, -1)],
                                     [(1, 1), (2, 1), (-1, 0)],
                                     [(1, 1), (1, 0), (0, 1)]]

        for test_case_arrangement in [head_neck_list_cross_edge, head_neck_list_not_cross_edge]:
            for [head, neck, direction] in test_case_arrangement:
                self.assertEqual(snake.get_head_neck_diff(head, neck), direction)

    def test_head_location(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.assertEqual(snake.head_location(), snake.body_queue[0])

    def test_next_step(self):
        # arrange
        init_body_length = 1
        board_dimension = 15
        snake = Snake(init_body_length=init_body_length, board_dimension=board_dimension)
        head_location = snake.head_location()
        key_to_tuple = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}

        # act and assert
        snake.set_move_direction(key_to_tuple['Left'])
        self.assertEqual(snake.move_direction, key_to_tuple['Left'])
        self.assertEqual(snake.next_step(), (head_location[0], (head_location[1] - 1) % board_dimension))

        snake.set_move_direction(key_to_tuple['Up'])
        self.assertEqual(snake.move_direction, key_to_tuple['Up'])
        self.assertEqual(snake.next_step(), ((head_location[0] - 1) % board_dimension, head_location[1]))

        snake.set_move_direction(key_to_tuple['Right'])
        self.assertEqual(snake.move_direction, key_to_tuple['Right'])
        self.assertEqual(snake.next_step(), (head_location[0], (head_location[1] + 1) % board_dimension))

        snake.set_move_direction(key_to_tuple['Down'])
        self.assertEqual(snake.move_direction, key_to_tuple['Down'])
        self.assertEqual(snake.next_step(), ((head_location[0] + 1) % board_dimension, head_location[1]))

    def test_move(self):
        # test normal move
        # arrange
        snake = Snake(init_body_length=1, board_dimension=3)
        snake.body_queue = deque([(1, 1), (0, 1)])
        snake.body_table = {(1, 1): 1, (0, 1): 1}
        snake.move_direction = (1, 0)

         # act
        snake.move(hit_fruit=False)

        # assert
        self.assertEqual(snake.body_queue, deque([(2, 1), (1, 1)]))
        self.assertEqual(snake.body_table, {(2, 1): 1, (1, 1): 1})
        self.assertEqual(snake.get_body_length(), 2)
        self.assertEqual(snake.is_bite_self(), False)

        # test hit fruit move
        # arrange
        snake = Snake(init_body_length=1, board_dimension=3)
        snake.body_queue = deque([(1, 1), (0, 1)])
        snake.body_table = {(1, 1): 1, (0, 1): 1}
        snake.move_direction = (1, 0)

         # act
        snake.move(hit_fruit=True)

        # assert
        self.assertEqual(snake.body_queue, deque([(2, 1), (1, 1), (0, 1)]))
        self.assertEqual(snake.body_table, {(2, 1): 1, (1, 1): 1, (0, 1): 1})
        self.assertEqual(snake.get_body_length(), 3)
        self.assertEqual(snake.is_bite_self(), False)

        # test bite self move
        # arrange
        snake = Snake(init_body_length=1, board_dimension=3)
        snake.body_queue = deque([(1, 1), (0, 1), (0, 0), (1, 0), (2, 0)])
        snake.body_table = {(1, 1): 1, (0, 1): 1, (0, 0): 1, (1, 0): 1, (2, 0): 1}
        snake.move_direction = (0, -1)

         # act
        snake.move(hit_fruit=False)

        # assert
        self.assertEqual(snake.body_queue, deque([(1, 0), (1, 1), (0, 1), (0, 0), (1, 0)]))
        self.assertEqual(snake.body_table, {(1, 1): 1, (0, 1): 1, (0, 0): 1, (1, 0): 2})
        self.assertEqual(snake.get_body_length(), 5)
        self.assertEqual(snake.is_bite_self(), True)

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


