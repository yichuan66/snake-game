from unittest import TestCase
from snake_game import *

class TestGame(TestCase):
    def test_run(self):
        # arrange

        # act

        # assert
        pass

    def test_update_frame(self):
        # arrange

        # act

        # assert
        pass

    def test_draw_game_state(self):
        # arrange

        # act

        # assert
        pass

    def test_terminate_game(self):
        # arrange

        # act

        # assert
        pass


class TestGameModel(TestCase):
    def test_update_game_state(self):
        # arrange

        # act

        # assert
        pass

    def test_get_game_state(self):
        # arrange

        # act

        # assert
        pass

    def test_draw_board(self):
        # arrange

        # act

        # assert
        pass

    def test_draw_snake(self):
        # arrange

        # act

        # assert
        pass

    def test_draw_fruit(self):
        # arrange

        # act

        # assert
        pass

    def test_print_game_state(self):
        # arrange

        # act

        # assert
        pass

    def test_is_snake_bite_self(self):
        # arrange

        # act

        # assert
        pass

    def test_get_board_dimension(self):
        # arrange

        # act

        # assert
        pass

    def test_get_snake_length(self):
        # arrange

        # act

        # assert
        pass


class TestBoard(TestCase):
    def test_get_dimension(self):
        # arrange

        # act

        # assert
        pass

    def test_has_fruit_on_spot(self):
        # arrange

        # act

        # assert
        pass

    def test_get_fruit_location(self):
        # arrange

        # act

        # assert
        pass

    def test_set_fruit_eaten(self):
        # arrange

        # act

        # assert
        pass

    def test_is_fruit_eaten(self):
        # arrange

        # act

        # assert
        pass

    def test_generate_new_fruit(self):
        # arrange

        # act

        # assert
        pass

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
        # arrange
        pass

    def test_get_current_direction(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act and assert
        pass

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

        # cross-board-edge case
        head = (1, 0)
        neck = (1, 2)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (0, 1))
        head = (1, 2)
        neck = (1, 0)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (0, -1))
        head = (0, 1)
        neck = (2, 1)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (1, 0))
        head = (2, 1)
        neck = (0, 1)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (-1, 0))

        # not-cross-board-edge case
        head = (1, 1)
        neck = (0, 1)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (1, 0))
        head = (1, 1)
        neck = (1, 2)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (0, -1))
        head = (1, 1)
        neck = (2, 1)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (-1, 0))
        head = (1, 1)
        neck = (1, 0)
        self.assertEqual(snake.get_head_neck_diff(head, neck), (0, 1))

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
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        pass

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
        pass

    def test_draw_game_state(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        pass


class TestGameController(TestCase):
    def test_set_input(self):
        # arrange

        # act

        # assert
        pass

    def test_get_input(self):
        # arrange

        # act

        # assert
        pass

    def test_clear_input(self):
        # arrange

        # act

        # assert
        pass


