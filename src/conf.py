# WINDOW
WIN_WIDTH, WIN_HEIGHT = 900, 500  # 900, 500
WIN_SIZE = WIN_WIDTH, WIN_HEIGHT


# WALL
WALL_COLOR = "B"
WALL_WIDTH = 10


# SPACESHIP
SPACESHIP_SPEED = 5
SPACESHIP_HEALTH = 10
WIDTH_THRESHOLD = 100
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SPACESHIP_SIZE = SPACESHIP_WIDTH, SPACESHIP_HEIGHT


# BULLET
BULLETS_MAX = 3
BULLET_FACTOR = 2
BULLET_SPEED = int(BULLET_FACTOR * SPACESHIP_SPEED)
BULLET_WIDTH = 10
BULLET_HEIGHT = 5

# FILES
ASSETS_FOLDER = "./assets"
y_spaceship_fn = "spaceship_yellow.png"
r_spaceship_fn = "spaceship_red.png"
bg_fn = "space.png"


# COLOR
COLOR = {
    "B": (0, 0, 0),  # black
    "w": (255, 255, 255),  # white
    "g": (0, 255, 0),  # greed
    "r": (255, 0, 0),  # red
    "b": (0, 0, 255),  # blue
    "y": (255, 255, 0),  # yellow
    "p": (128, 0, 128),  # purple
    "f": (255, 0, 255),  # fushia
    "s": (192, 192, 192),  # silver
    "o": (128, 128, 0),  # olive green darj
    "n": (0, 0, 128),  # navy dark_blue
}

# FPS
FPS = 60  # 60
