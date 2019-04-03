from unittest import TestCase
from snake_game import *

class TestGame(TestCase):
    def test_run(self):
        self.fail()

    def test_update_frame(self):
        self.fail()

    def test_draw_game_state(self):
        self.fail()

    def test_terminate_game(self):
        self.fail()


class TestGameModel(TestCase):
    def test_update_game_state(self):
        self.fail()

    def test_get_game_state(self):
        self.fail()

    def test_draw_board(self):
        self.fail()

    def test_draw_snake(self):
        self.fail()

    def test_draw_fruit(self):
        self.fail()

    def test_print_game_state(self):
        self.fail()

    def test_is_snake_bite_self(self):
        self.fail()

    def test_get_board_dimension(self):
        self.fail()

    def test_get_snake_length(self):
        self.fail()


class TestBoard(TestCase):
    def test_get_dimension(self):
        self.fail()

    def test_has_fruit_on_spot(self):
        self.fail()

    def test_get_fruit_location(self):
        self.fail()

    def test_set_fruit_eaten(self):
        self.fail()

    def test_is_fruit_eaten(self):
        self.fail()

    def test_generate_new_fruit(self):
        self.fail()


class TestSnake(TestCase):
    def test_initialize_body(self):
        self.fail()

    def test_set_new_direction(self):
        self.fail()

    def test_get_direction(self):
        self.fail()

    def test_head_location(self):
        self.fail()

    def test_next_step(self):
        self.fail()

    def test_move(self):
        self.fail()

    def test_is_bite_self(self):
        self.fail()

    def test_get_body_length(self):
        self.fail()


class TestGameView(TestCase):
    def test_draw_square(self):
        self.fail()

    def test_draw_game_state(self):
        self.fail()


class TestGameController(TestCase):
    def test_set_input(self):
        self.fail()

    def test_get_input(self):
        self.fail()

    def test_clear_input(self):
        self.fail()
