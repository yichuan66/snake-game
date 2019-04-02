from collections import deque
from random import randint
import sys
from tkinter import *

class Game:
    def __init__(self, board_dimension=15, init_snake_length=1, delay=50):
        self.tk = Tk()
        self.delay = delay

        self.model = GameModel(board_dimension=board_dimension, init_snake_length=init_snake_length)
        self.view = GameView(tk=self.tk, board_dimension=self.model.get_board_dimension())
        self.controller = GameController(tk=self.tk)

    def run(self):
        self.update_frame()
        self.tk.mainloop()

    def update_frame(self):
        self.tk.after(self.delay, self.update_frame)

        self.model.update_game_state(dir_input=self.controller.get_input())

        if self.model.is_snake_bite_self():
            self.terminate_game()
        self.controller.clear_input()

        self.draw_game_state()

    def draw_game_state(self):
        game_state = self.model.get_game_state()
        self.view.draw_game_state(game_state)

    def terminate_game(self):
        print("YOUR FINAL LENGTH:", self.model.get_snake_length())
        exit()

class GameModel:
    """

    """

    def __init__(self, board_dimension=15, init_snake_length=1):
        self.board = Board(board_dimension)
        self.snake = Snake(init_snake_length, board_dimension)
        self.game_state = list()

    def update_game_state(self, dir_input):
        """

        :param dir_input:
        """
        self.snake.set_new_direction(dir_input)
        hit_fruit = (self.snake.next_step() == self.board.get_fruit_location())
        self.snake.move(hit_fruit=hit_fruit)

        if hit_fruit:
            self.board.set_fruit_eaten()

        if self.board.is_fruit_eaten():
            self.board.generate_new_fruit(self.snake.body_table)

    def get_game_state(self):
        """

        :return:
        """
        self.draw_board()
        self.draw_snake()
        self.draw_fruit()
        return self.game_state

    def draw_board(self):
        """

        """
        self.game_state.clear()
        for i in range(0, self.board.get_dimension()):
            row = list()
            for j in range(0, self.board.get_dimension()):
                row.append(0)
            self.game_state.append(row)

    def draw_snake(self):
        """

        """
        for body_loc in self.snake.body_queue:
            self.game_state[body_loc[0]][body_loc[1]] = 1

    def draw_fruit(self):
        """

        :return:
        """
        i, j = self.board.get_fruit_location()
        if (i, j) == (-1, -1):
            return
        self.game_state[i][j] = 2

    def print_game_state(self):
        """

        """
        for row in self.game_state:
            for pixel in row:
                sys.stdout.write(str(pixel) + " ")
            print()

    def is_snake_bite_self(self):
        """

        :return:
        """
        return self.snake.is_bite_self()

    def get_board_dimension(self):
        """

        :return:
        """
        return self.board.get_dimension()

    def get_snake_length(self):
        """

        :return:
        """
        return self.snake.get_body_length()


class Board:
    """

    """

    def __init__(self, dimension):
        self.dimension = dimension
        self.fruit_location = (-1, -1)

    def get_dimension(self):
        """

        :return:
        """
        return self.dimension

    def has_fruit_on_spot(self, location):
        """

        :param location:
        :return:
        """
        return location == self.fruit_location

    def get_fruit_location(self):
        """

        :return:
        """
        return self.fruit_location

    def set_fruit_eaten(self):
        """

        """
        self.fruit_location = (-1, -1)

    def is_fruit_eaten(self):
        """

        :return:
        """
        return self.fruit_location == (-1, -1)

    def generate_new_fruit(self, snake_body):
        """

        :param snake_body:
        """
        while self.fruit_location == (-1, -1) or self.fruit_location in snake_body:
            i = randint(0, self.dimension - 1)
            j = randint(0, self.dimension - 1)
            self.fruit_location = (i, j)


class Snake:
    """

    """

    def __init__(self, init_body_length, board_dimension):
        self.init_body_length = init_body_length
        self.board_dimension = board_dimension
        self.direction = "Down"
        self.direction_table = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
        self.body_queue = deque()
        self.body_table = set()
        self.bite_self = False

        self.initialize_body()

    def initialize_body(self):
        """

        """
        for i in range(0, self.init_body_length):
            loc = tuple((i, 0))
            self.body_queue.appendleft(loc)
            self.body_table.add(loc)
        print(len(self.body_queue))

    def set_new_direction(self, input_direction):
        """

        :param input_direction:
        :return:
        """
        if input_direction not in self.direction_table:
            return
        if (self.direction_table[input_direction][0] + self.direction_table[self.direction][0],
            self.direction_table[input_direction][1] + self.direction_table[self.direction][1]) == (0, 0):
            return
        self.direction = input_direction

    def get_direction(self):
        """

        :return:
        """
        return self.direction

    def head_location(self):
        """

        :return:
        """
        return self.body_queue[0]

    def next_step(self):
        """

        :return:
        """
        head = self.body_queue[0]
        return ((head[0] + self.direction_table[self.direction][0]) % self.board_dimension,
                (head[1] + self.direction_table[self.direction][1]) % self.board_dimension)

    def move(self, hit_fruit):
        """

        :param hit_fruit:
        """
        next_step = self.next_step()

        if not hit_fruit:
            tail = self.body_queue.pop()
            self.body_table.remove(tail)

        if next_step in self.body_table:
            self.bite_self = True

        self.body_queue.appendleft(next_step)
        self.body_table.add(next_step)

    def is_bite_self(self):
        """

        :return:
        """
        return self.bite_self

    def get_body_length(self):
        """

        :return:
        """
        return len(self.body_queue)

class GameView:
    """

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

        :param loc_i:
        :param loc_j:
        :param line_width:
        :param fill:
        """
        side_length = self.square_size
        y1 = loc_i * side_length + line_width
        x1 = loc_j * side_length + line_width
        y2 = (loc_i + 1) * side_length
        x2 = (loc_j + 1) * side_length
        self.canvas.create_rectangle(x1, y1, x2, y2, width=line_width, fill=fill)

    def draw_game_state(self, game_state):
        """

        :param game_state:
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

    """

    def __init__(self, tk):
        self.tk = tk
        self.is_command_loaded = False
        self.key = 'Down'
        self.no_input = 'None'
        self.tk.bind('<Key>', self.set_input)

    def set_input(self, event):
        """

        :param event:
        """
        input_key = event.keysym
        if self.key == self.no_input:
            self.key = input_key

    def get_input(self):
        """

        :return:
        """
        return self.key

    def clear_input(self):
        """

        """
        self.key = self.no_input


def main():
    """

    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
