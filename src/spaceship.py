import os
import pygame

from src.conf import *
from src.bullet import Bullet


class SpaceShip(pygame.Rect):
    """our spaceship Object"""

    def __init__(self, color, filename, board):
        """init method"""

        # color and rotate
        self.color = color
        rotate = -90 if "r" in color else 90

        # Rect
        self.height = SPACESHIP_HEIGHT
        self.width = SPACESHIP_WIDTH
        self.size = (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)

        center = (WIN_HEIGHT // 2) - (SPACESHIP_HEIGHT // 2)

        w = (
            WIDTH_THRESHOLD
            if rotate == 90
            else WIN_WIDTH - WIDTH_THRESHOLD + (WIDTH_THRESHOLD // 2)
        )

        # self.position = w, center

        pygame.Rect.__init__(self, w, center, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

        # self.position = pygame.Rect(w, center, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

        # controls
        self.controls = (
            [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
            if "r" in color
            else [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]
        )

        # image
        self.filename = filename

        self.image = pygame.image.load(os.path.join(ASSETS_FOLDER, filename))
        self.image = pygame.transform.scale(self.image, SPACESHIP_SIZE)
        self.image = pygame.transform.rotate(self.image, rotate)

        # properties
        self.health = SPACESHIP_HEALTH
        self.speed = SPACESHIP_SPEED

        # board
        self.board = board

        # bullets
        self.bullet_list = []

    def moove_up(self):
        """up"""

        cond = self.top > self.board.top
        if cond:
            self.y -= self.speed

    def moove_down(self):
        """down"""

        cond = self.bottom <= WIN_HEIGHT - (self.height // 2)
        if cond:
            self.y += self.speed

    def moove_left(self):
        """left"""

        if self.color == "r":
            cond = self.left > (self.board.wall.left + self.speed)
        else:
            cond = self.left > 0

        if cond:
            self.x -= self.speed

    def moove_right(self):
        """right"""

        cond1 = self.right <= WIN_WIDTH + (self.width // 2) - self.speed - 1

        if self.color == "r":
            cond = self.right <= WIN_WIDTH + (self.width // 2) - self.speed - 1
        else:
            cond = self.right < self.board.wall.left

        if cond:
            self.x += self.speed

    def moove(self, keys_pressed):
        """make moove"""
        if keys_pressed[self.controls[0]]:
            self.moove_up()
        if keys_pressed[self.controls[1]]:
            self.moove_down()
        if keys_pressed[self.controls[2]]:
            self.moove_left()
        if keys_pressed[self.controls[3]]:
            self.moove_right()

    def fire(self):
        """ """

        if len(self.bullet_list) < BULLETS_MAX:
            bullet = Bullet(self.color, self.x, self.centery + (BULLET_HEIGHT // 2))
            self.bullet_list.append(bullet)

    def update_bullets(self):
        """ """

        # moove bullets
        for bullet in self.bullet_list:
            bullet.moove()

        # delete bullet if needed
        for bullet in self.bullet_list:

            # cond
            cond = WIN_WIDTH > bullet.x > 0
            if (not cond) or not (bullet.is_live):
                self.bullet_list.remove(bullet)
                del bullet
