from unittest import TestCase
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
        self.assertEqual(snake.direction, 'Down')
        self.assertEqual(snake.direction_table, {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)})
        self.assertEqual(type(snake.body_queue), deque)
        self.assertEqual(type(snake.body_table), set)
        self.assertEqual(snake.bite_self, False)

        for i in range(0, init_body_length):
            loc = tuple((i, 0))
            self.assertTrue(loc in snake.body_table)
            self.assertTrue(snake.body_queue[init_body_length - i - 1] == loc)

    def test_set_new_direction(self):
        # arrange
        snake = Snake(init_body_length=1, board_dimension=15)
        self.assertEqual(snake.direction, 'Down')

        # set directions
        snake.set_new_direction('Left')
        self.assertEqual(snake.direction, 'Left')
        # the setter should ignore opposite direction setting
        snake.set_new_direction('Right')
        self.assertEqual(snake.direction, 'Left')

        # act and assert

        # set directions
        snake.set_new_direction('Up')
        self.assertEqual(snake.direction, 'Up')
        # the setter should ignore opposite direction setting
        snake.set_new_direction('Down')
        self.assertEqual(snake.direction, 'Up')

        # set directions
        snake.set_new_direction('Right')
        self.assertEqual(snake.direction, 'Right')
        # the setter should ignore opposite direction setting
        snake.set_new_direction('Left')
        self.assertEqual(snake.direction, 'Right')

        # set directions
        snake.set_new_direction('Down')
        self.assertEqual(snake.direction, 'Down')
        # the setter should ignore opposite direction setting
        snake.set_new_direction('Up')
        self.assertEqual(snake.direction, 'Down')

    def test_get_direction(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act and assert
        snake.set_new_direction('Left')
        self.assertEqual(snake.get_direction(), 'Left')

        snake.set_new_direction('Up')
        self.assertEqual(snake.get_direction(), 'Up')

        snake.set_new_direction('Right')
        self.assertEqual(snake.get_direction(), 'Right')

        snake.set_new_direction('Down')
        self.assertEqual(snake.get_direction(), 'Down')

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

        # act and assert
        snake.set_new_direction('Left')
        self.assertEqual(snake.get_direction(), 'Left')
        self.assertEqual(snake.next_step(), (head_location[0], (head_location[1] - 1)%board_dimension) )

        snake.set_new_direction('Up')
        self.assertEqual(snake.get_direction(), 'Up')
        self.assertEqual(snake.next_step(), ((head_location[0] - 1)%board_dimension, head_location[1]) )

        snake.set_new_direction('Right')
        self.assertEqual(snake.get_direction(), 'Right')
        self.assertEqual(snake.next_step(), (head_location[0], (head_location[1] + 1)%board_dimension) )

        snake.set_new_direction('Down')
        self.assertEqual(snake.get_direction(), 'Down')
        self.assertEqual(snake.next_step(), ((head_location[0] + 1)%board_dimension, head_location[1]) )

    def test_move(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.fail()

    def test_is_bite_self(self):
        # arrange
        snake = Snake(init_body_length=5, board_dimension=15)

        # act

        # assert
        self.assertEqual(snake.is_bite_self(), snake.bite_self)

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
