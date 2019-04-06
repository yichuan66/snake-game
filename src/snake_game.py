# coding=utf-8

"""
Description: A snake game
"""

from collections import deque
from random import randint
import sys
from tkinter import *

class Game:
    """
    The game class that controls and monitor
    """
    def __init__(self, board_dimension=15, init_snake_length=1, delay=50):
        self.tk = Tk()
        self.delay = delay

        self.model = GameModel(board_dimension=board_dimension, init_snake_length=init_snake_length)
        self.view = GameView(tk=self.tk, board_dimension=self.model.get_board_dimension())
        self.controller = GameController(tk=self.tk)

    def run(self):
        """
        Run the game
        """
        self.update_frame()
        self.tk.mainloop()

    def update_frame(self):
        """
        Update one frame
        """
        self.tk.after(self.delay, self.update_frame)

        self.model.update_game_state(dir_input=self.controller.get_input_direction())

        if self.model.is_snake_bite_self():
            self.terminate_game()
        self.controller.clear_input()

        self.draw_game_state()

    def draw_game_state(self):
        """
        Draw the current game state
        """
        game_state = self.model.get_game_state()
        self.view.draw_game_state(game_state)

    def terminate_game(self):
        """
        Terminate the game
        """
        print("YOUR FINAL LENGTH:", self.model.get_snake_length())
        exit()

class GameModel:
    """
    The model that describes the game's internal state
    """

    def __init__(self, board_dimension=15, init_snake_length=1):
        self.board = Board(board_dimension)
        self.snake = Snake(init_snake_length, board_dimension)
        self.game_state = list()

    def update_game_state(self, dir_input):
        """
        Update the game state with direction input

        :param dir_input: the user specified input (a direction)
        """

        if(dir_input != (0, 0)):
            self.snake.set_move_direction(dir_input)
        hit_fruit = (self.snake.next_step() == self.board.get_fruit_location())
        self.snake.move(hit_fruit=hit_fruit)

        if hit_fruit:
            self.board.set_fruit_eaten()

        if self.board.is_fruit_eaten():
            self.board.generate_new_fruit(self.snake.body_table)

    def get_game_state(self):
        """
        Return current game state as a 2D list

        :return: Current game state (2D list)
        """
        self.draw_board()
        self.draw_snake()
        self.draw_fruit()
        return self.game_state

    def draw_board(self):
        """
        Draw an empty board
        """
        self.game_state.clear()
        for i in range(0, self.board.get_dimension()):
            row = list()
            for j in range(0, self.board.get_dimension()):
                row.append(0)
            self.game_state.append(row)

    def draw_snake(self):
        """
        Draw snake on the board
        """
        for body_loc in self.snake.body_queue:
            self.game_state[body_loc[0]][body_loc[1]] = 1

    def draw_fruit(self):
        """
        Draw fruit on the board

        :return: No drawing if there is no fruit (-1, -1)
        """
        i, j = self.board.get_fruit_location()
        if (i, j) == (-1, -1):
            return
        self.game_state[i][j] = 2

    def print_game_state(self):
        """
        Print out current game state to the console (as a 2D list)
        """
        for row in self.game_state:
            for pixel in row:
                sys.stdout.write(str(pixel) + " ")
            print()

    def is_snake_bite_self(self):
        """
        Return whether the snake bites itself

        :return: whether the snake bites itself
        """
        return self.snake.is_bite_self()

    def get_board_dimension(self):
        """
        Return the board dimension

        :return: The board dimension
        """
        return self.board.get_dimension()

    def get_snake_length(self):
        """
        Return the snake's body length

        :return: The snake's body length
        """
        return self.snake.get_body_length()


class Board:
    """
    A 2D board for snake game
    """

    def __init__(self, dimension):
        self.dimension = dimension
        self.fruit_location = (-1, -1)

    def get_dimension(self):
        """
        Return the board dimension

        :return: The board dimension
        """
        return self.dimension

    def has_fruit_on_spot(self, location):
        """
        Check whether there is a fruit at this location

        :param location: The location to be checked
        :return: Whether there is a fruit at this location
        """
        return location == self.fruit_location

    def get_fruit_location(self):
        """
        Return the fruit location

        :return: The fruit location
        """
        return self.fruit_location

    def set_fruit_eaten(self):
        """
        Set the fruit as eaten
        """
        self.fruit_location = (-1, -1)

    def is_fruit_eaten(self):
        """
        Check if the fruit is eaten

        :return: If the fruit is eaten
        """
        return self.fruit_location == (-1, -1)

    def generate_new_fruit(self, snake_body):
        """
        Generate a new fruit on the board

        :param snake_body: The snake's body position (to be avoided by fruit generation)
        """
        while self.fruit_location == (-1, -1) or self.fruit_location in snake_body:
            i = randint(0, self.dimension - 1)
            j = randint(0, self.dimension - 1)
            self.fruit_location = (i, j)


class Snake:
    """
    The snake class that describes the body length, location and movement of a snake on 2D board
    The snake only accepts board that has >=3 side lengths
    The snake only accepts body length larger than 0
    """

    def __init__(self, init_body_length=1, board_dimension=15):
        self.init_body_length = init_body_length
        self.board_dimension = board_dimension
        self.move_direction = (1, 0)
        self.body_queue = deque()
        self.body_table = dict()

        self.initialize_body()

    def initialize_body(self):
        """
        Initialize a body on the board
        """
        for i in range(0, self.init_body_length):
            loc = tuple((i, 0))
            self.body_queue.appendleft(loc)
            self.body_table[loc] = 1

    def set_move_direction(self, input_direction):
        """
        Set new direction of motion.

        :param input_direction: New direction (0, 1), (0, -1), (1, 0), (-1, 0)
        :return: Do nothing if the new direction is the exact opposite of current direction
        """

        if self.get_body_length() == 1 or  \
                not self.is_opposite_direction(input_direction, self.get_current_direction()):
            self.move_direction = input_direction


    def is_opposite_direction(self, d1, d2):
        """
        Determine if two direction are opposites of each other
        :param d1: direction1
        :param d2: direction2        
        :return: True if the input directions are opposite
        """
        return d1[0] + d2[0] == 0 and d1[1] + d2[1] == 0

    def get_current_direction(self):
        """
        Return current motion direction by calculating the position difference between head and neck
        (board edge overflow taken into account)

        Note: this method only works well when both board side lengths >=3

        :return: Current motion direction
        """
        if len(self.body_queue) == 1:
            return self.move_direction

        head = self.body_queue[0]
        neck = self.body_queue[1]

        return self.get_head_neck_diff(head, neck)

    def get_head_neck_diff(self, head, neck):
        """
        Return the head-neck location difference (board edge overflow taken into account)

        :param head: head location
        :param neck: neck location (the element following the head in queue)
        :return: head-neck location difference
        """
        i_diff = head[0] - neck[0]
        j_diff = head[1] - neck[1]

        if i_diff > 1: i_diff -= self.board_dimension
        if i_diff < -1: i_diff += self.board_dimension
        if j_diff > 1: j_diff -= self.board_dimension
        if j_diff < -1: j_diff += self.board_dimension

        return i_diff, j_diff

    def head_location(self):
        """
        Return the snake's head location

        :return: The snake's head location
        """
        return self.body_queue[0]

    def next_step(self):
        """
        Return snake's next head location if following current direction.

        :return: Snake's next head location if following current direction.
        """
        head = self.body_queue[0]
        return ((head[0] + self.move_direction[0]) % self.board_dimension,
                (head[1] + self.move_direction[1]) % self.board_dimension)

    def move(self, hit_fruit):
        """
        Move one step

        :param hit_fruit: Whether the snake hits a fruit with this motion
        """
        next_step = self.next_step()

        if not hit_fruit:
            tail = self.body_queue.pop()
            self.body_table.pop(tail)

        self.body_queue.appendleft(next_step)
        if(next_step in self.body_table):
            self.body_table[next_step] += 1
        else:
            self.body_table[next_step] = 1

    def is_bite_self(self):
        """
        Return if the snake bites itself.

        :return: Whether the snake bites itself.
        """
        return max(self.body_table.values()) > 1

    def get_body_length(self):
        """
        Return the body length

        :return: The body length
        """
        return len(self.body_queue)

class GameView:
    """
    The game view that converts the game state to visual display
    """

    def __init__(self,
                 tk,
                 board_dimension=15,
                 bg='white',
                 square_size=20,
                 snake_body_color='yellow',
                 fruit_color='red'):
        self.tk = tk
        self.width = square_size * board_dimension
        self.height = square_size * board_dimension
        self.bg = bg
        self.canvas = Canvas(master=self.tk, width=self.width, height=self.height, bg=bg)
        self.canvas.pack()
        self.square_size = square_size
        self.snake_body_color = snake_body_color
        self.fruit_color = fruit_color

    def draw_square(self, loc_i, loc_j, line_width=5, fill='blue'):
        """
        Draw a square on tk.Canvas()

        :param loc_i: Square's vertical coordinate
        :param loc_j: Square's horizontal coordinate
        :param line_width: Square's edge line width
        :param fill: Fill color
        """
        side_length = self.square_size
        y1 = loc_i * side_length + line_width
        x1 = loc_j * side_length + line_width
        y2 = (loc_i + 1) * side_length
        x2 = (loc_j + 1) * side_length
        self.canvas.create_rectangle(x1, y1, x2, y2, width=line_width, fill=fill)

    def draw_game_state(self, game_state):
        """
        Draw the game state (from model) onto the canvas

        :param game_state: Current game state
        """
        self.canvas.delete("all")
        for i in range(len(game_state)):
            for j in range(len(game_state)):
                pix = game_state[i][j]
                if pix == 1:
                    self.draw_square(i, j, fill=self.snake_body_color)
                elif pix == 2:
                    self.draw_square(i, j, fill=self.fruit_color)


class GameController:
    """
    The game controller that takes user input event and provides the input to view and model
    """

    def __init__(self, tk):
        self.tk = tk
        self.is_command_loaded = False
        self.no_input = 'None'
        self.key = self.no_input
        self.tk.bind('<Key>', self.set_input)
        self.key_to_tuple = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1), 'None': (0, 0)}

    def set_input(self, event):
        """
        Set user input according to event

        :param event: User input event (key board hit -- up, down, left, right)
        """
        input_key = event.keysym
        if self.key == self.no_input:
            self.key = input_key

    def get_input_direction(self):
        """
        Return the first different user input in current after input clear up

        :return: The first different user input in current after input clear up
        """
        if self.key in self.key_to_tuple:
            return self.key_to_tuple[self.key]
        return self.key_to_tuple[self.no_input]

    def clear_input(self):
        """
        Reset user input to no input
        """
        self.key = self.no_input


def main():
    """
    Main function
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
