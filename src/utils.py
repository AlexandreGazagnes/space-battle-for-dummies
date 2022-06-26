import os
import pygame

from src.conf import *


def manage_collistions(yellow, red, board):
    """ """

    # yellow vs red
    for bullet in yellow.bullet_list:
        if red.colliderect(bullet):
            red.health -= 1
            yellow.bullet_list.remove(bullet)

    # red vs yellow
    for bullet in red.bullet_list:
        if yellow.colliderect(bullet):
            yellow.health -= 1
            red.bullet_list.remove(bullet)

    board.update_heath(yellow, red)


def manage_endgame(run, yellow, red):

    if not run:
        return 0

    if yellow.health == 0:
        print("red wins")
        return 0

    if red.health == 0:
        print("yellow wins")
        return 0

    return 1


def draw_window(board, WIN, yellow, red):
    """color window and update"""

    # bg
    # if not color:
    #     color = random.choice(list(COLOR.values()))
    # WIN.fill(color)

    WIN.blit(board.bg_image, board)
    pygame.draw.rect(WIN, board.wall_color, board.wall)

    # spaceship
    WIN.blit(yellow.image, yellow)
    WIN.blit(red.image, red)

    # bullets
    for bullet in yellow.bullet_list:
        pygame.draw.rect(WIN, COLOR[bullet.color], bullet)
    for bullet in red.bullet_list:
        pygame.draw.rect(WIN, COLOR[red.color], bullet)

    # score
    WIN.blit(board.yellow_health, (10, 10))
    WIN.blit(board.red_health, (WIN_WIDTH // 2 + 10, 10))

    # update
    pygame.display.update()
