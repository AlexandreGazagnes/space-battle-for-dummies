import os
import pygame
from src.conf import *


class Board(pygame.Rect):
    "board class"

    def __init__(self, image_fn, font):
        """ """

        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.size = WIN_WIDTH, WIN_HEIGHT

        pygame.Rect.__init__(self, 0, 0, WIN_WIDTH, WIN_HEIGHT)

        self.bg_image_fn = image_fn
        self.bg_image = pygame.image.load(os.path.join(ASSETS_FOLDER, image_fn))
        self.bg_image = pygame.transform.scale(self.bg_image, self.size)

        self.wall_color = COLOR[WALL_COLOR]
        self.wall = pygame.Rect(
            (WIN_WIDTH // 2) - (WALL_WIDTH // 2), 0, WALL_WIDTH, WIN_HEIGHT
        )

        self.font = font
        self.yellow_health = font.render("HEALTH", False, (0, 0, 0))
        self.red_health = font.render("HEALTH", False, (0, 0, 0))

    def update_heath(self, yellow, red):
        """ """

        yellow_text = f"HEALTH : {yellow.health}"
        self.yellow_health = self.font.render(yellow_text, False, (0, 0, 0))

        red_text = f"HEALTH : {red.health}"
        self.red_health = self.font.render(red_text, False, (0, 0, 0))
