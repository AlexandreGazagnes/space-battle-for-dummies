import os
import pygame

from src.conf import *


class Bullet(pygame.Rect):
    """our bullets Object"""

    def __init__(self, color, x, y):
        """ """

        self.color = color
        self.speed = BULLET_SPEED
        pygame.Rect.__init__(self, x, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.is_live = 1

    def moove(self):
        """moove"""

        if self.color == "y":
            self.x += BULLET_SPEED
        else:
            self.x -= BULLET_SPEED
