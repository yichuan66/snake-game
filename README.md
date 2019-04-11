# snake-game
This is a basic snake game for me to get familiar with Python and general software development practices such as version control, testing, development cycle, refactoring, etc...

Runs on Python 3

The game is playable.
Use direction key to control the snake.
set your own delay to adjust game speed. The delay between frame is in milliseconds.
Default is 50. Smaller delay means faster pace.

Opposite direction allowed when you are 1 cell long. You can't go backwards when
you are more than one cell long.
Open by running "python snake_game.py" in cmd.

TO-DO on next release:
Unit testing is currently 30% done. Finish unit testing. Unit testing is not finished in this release because
the model, view and controller are tricky to test and that I'm lazy.

Add exceptions if I have time and interest to do so.

Get a better fruit generation algorithm. The current one doesn't work well when the
snake fills a high portion of board space.

