from collections import deque
from random import randint
import sys
import tkinter


# noinspection PyMissingOrEmptyDocstring,PyPep8Naming,PyPep8Naming
class Game:
    def __init__(self, boardDimension=15, initSnakeLength=1, delay=50):
        self.tk = Tk()
        self.delay = delay

        self.model = GameModel(boardDimension=boardDimension, initSnakeLength=initSnakeLength)
        self.view = GameView(tk=self.tk, boardDimension=self.model.GetBoardDimeision())
        self.controller = GameController(tk=self.tk)

    def Run(self):
        self.UpdateFrame()
        self.tk.mainloop()

    def UpdateFrame(self):
        self.tk.after(self.delay, self.UpdateFrame)

        self.model.UpdateGameState(dirInput=self.controller.GetInput())

        if self.model.IsSnakeBiteSelf():
            self.TerminateGame()
        self.controller.ClearInput()

        self.DrawGameState()

    def DrawGameState(self):
        gameState = self.model.GetGameState()
        self.view.DrawGamegameState(gameState)

    def TerminateGame(self):
        print("YOUR FINAL LENGTH:", self.model.GetSnakeLength())
        exit()


# noinspection PyRedundantParentheses,PyPep8Naming
class GameModel:
    """

    """

    def __init__(self, boardDimension=15, initSnakeLength=1):
        self.board = Board(boardDimension)
        self.snake = Snake(initSnakeLength, boardDimension)
        self.gameState = list()

    def UpdateGameState(self, dirInput):
        """

        :param dirInput:
        """
        self.snake.SetNewDirection(dirInput)
        hitFruit = (self.snake.NextStep() == self.board.get_fruit_location())
        self.snake.Move(hitFruit=hitFruit)

        if hitFruit:
            self.board.set_fruit_eaten()

        if self.board.is_fruit_eaten():
            self.board.GenerateNewFruit(self.snake.bodyTable)

    def GetGameState(self):
        """

        :return:
        """
        self.DrawBoard()
        self.DrawSnake()
        self.DrawFruit()
        return self.gameState
        # self.PrintgameState() # debug purpose

    def DrawBoard(self):
        """

        """
        self.gameState.clear()
        for i in range(0, self.board.get_dimension()):
            row = list()
            for j in range(0, self.board.get_dimension()):
                row.append(0)
            self.gameState.append(row)

    # noinspection PyPep8Naming
    def DrawSnake(self):
        """

        """
        for bodyLoc in self.snake.bodyQueue:
            self.gameState[bodyLoc[0]][bodyLoc[1]] = 1

    def DrawFruit(self):
        """

        :return:
        """
        i, j = self.board.get_fruit_location()
        if (i, j) == (-1, -1):
            return
        self.gameState[i][j] = 2

    def PrintGameState(self):
        """

        """
        for row in self.gameState:
            for pixel in row:
                sys.stdout.write(str(pixel) + " ")
            print()

    def IsSnakeBiteSelf(self):
        """

        :return:
        """
        return self.snake.IsBiteSelf()

    def GetBoardDimeision(self):
        """

        :return:
        """
        return self.board.get_dimension()

    def GetSnakeLength(self):
        """

        :return:
        """
        return self.snake.GetBodyLength()


class Board:
    """

    """

    def __init__(self, dimension):
        self.dimension = dimension
        self.fruitLocation = (-1, -1)

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
        return location == self.fruitLocation

    def get_fruit_location(self):
        """

        :return:
        """
        return self.fruitLocation

    def set_fruit_eaten(self):
        """

        """
        self.fruitLocation = (-1, -1)

    def is_fruit_eaten(self):
        """

        :return:
        """
        return self.fruitLocation == (-1, -1)

    def GenerateNewFruit(self, snakeBody):
        """

        :param snakeBody:
        """
        while self.fruitLocation == (-1, -1) or self.fruitLocation in snakeBody:
            i = randint(0, self.dimension - 1)
            j = randint(0, self.dimension - 1)
            self.fruitLocation = (i, j)


class Snake:
    """

    """

    def __init__(self, initBodyLength, boardDimension):
        self.initBodyLength = initBodyLength
        self.boardDimension = boardDimension
        self.direction = "Down"
        self.directionTable = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
        self.bodyQueue = deque()
        self.bodyTable = set()
        self.biteSelf = False

        self.InitializeBody()

    def InitializeBody(self):
        """

        """
        for i in range(0, self.initBodyLength):
            loc = tuple((i, 0))
            self.bodyQueue.appendleft(loc)
            self.bodyTable.add(loc)
        print(len(self.bodyQueue))

    def SetNewDirection(self, dir):
        """

        :param dir:
        :return:
        """
        if dir not in self.directionTable:
            return
        if (self.directionTable[dir][0] + self.directionTable[self.direction][0],
            self.directionTable[dir][1] + self.directionTable[self.direction][1]) == (0, 0):
            return
        self.direction = dir

    def GetDirection(self):
        """

        :return:
        """
        return self.direction

    def HeadLocation(self):
        """

        :return:
        """
        return self.body[0]

    def NextStep(self):
        """

        :return:
        """
        head = self.bodyQueue[0]
        return ((head[0] + self.directionTable[self.direction][0]) % self.boardDimension,
                (head[1] + self.directionTable[self.direction][1]) % self.boardDimension)

    def Move(self, hitFruit):
        """

        :param hitFruit:
        """
        nextStep = self.NextStep()

        if not hitFruit:
            tail = self.bodyQueue.pop()
            self.bodyTable.remove(tail)

        if nextStep in self.bodyTable:
            self.biteSelf = True

        self.bodyQueue.appendleft(nextStep)
        self.bodyTable.add(nextStep)

    def IsBiteSelf(self):
        """

        :return:
        """
        return self.biteSelf

    def GetBodyLength(self):
        """

        :return:
        """
        return len(self.bodyQueue)


# noinspection SpellCheckingInspection
class GameView:
    """

    """

    def __init__(self, tk, boardDimension=15, bg='white', squareSize=20, snakeBodyColor='yellow', fruitColor='red'):
        self.tk = tk
        self.width = squareSize * boardDimension
        self.height = squareSize * boardDimension
        self.bg = bg
        self.canvas = Canvas(master=self.tk, width=self.width, height=self.height, bg=bg)
        self.canvas.pack()
        self.squareSize = squareSize
        self.snakeBodyColor = snakeBodyColor
        self.fruitColor = fruitColor

    def DrawSquare(self, loc_i, loc_j, lineWidth=5, fill='blue'):
        """

        :param loc_i:
        :param loc_j:
        :param lineWidth:
        :param fill:
        """
        sideLength = self.squareSize
        y1 = loc_i * sideLength + lineWidth
        x1 = loc_j * sideLength + lineWidth
        y2 = (loc_i + 1) * sideLength
        x2 = (loc_j + 1) * sideLength
        self.canvas.create_rectangle(x1, y1, x2, y2, width=lineWidth, fill=fill)

    def DrawGamegameState(self, gameState):
        """

        :param gameState:
        """
        self.canvas.delete("all")
        for i in range(len(gameState)):
            for j in range(len(gameState)):
                pix = gameState[i][j]
                if pix == 1:
                    self.DrawSquare(i, j, fill=self.snakeBodyColor)
                elif pix == 2:
                    self.DrawSquare(i, j, fill=self.fruitColor)


class GameController:
    """

    """

    def __init__(self, tk):
        self.tk = tk
        self.isCommandLoaded = False
        self.key = 'Down'
        self.noInput = 'None'
        self.tk.bind('<Key>', self.SetInput)

    def SetInput(self, event):
        """

        :param event:
        """
        inputKey = event.keysym
        if self.key == self.noInput:
            self.key = inputKey

    def GetInput(self):
        """

        :return:
        """
        return self.key

    def ClearInput(self):
        """

        """
        self.key = self.noInput


def main():
    """

    """
    game = Game()
    game.Run()


if __name__ == "__main__":
    main()
