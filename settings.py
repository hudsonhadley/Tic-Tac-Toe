from collections import namedtuple

Size = namedtuple("Size", ("width", "height"))
Color = namedtuple("Color", ("red", "green", "blue"))
Point = namedtuple("Point", ("x", "y"))

WINDOW_SIZE = Size(800, 600)

BACKGROUND_COLOR = Color(255, 255, 255)
BOARD_COLOR = Color(0, 0, 0)

BOARD_SIZE = Size(WINDOW_SIZE.height * 0.75, WINDOW_SIZE.height * 0.75)
SPOT_SIZE = Size(BOARD_SIZE.width // 3, BOARD_SIZE.height // 3)
