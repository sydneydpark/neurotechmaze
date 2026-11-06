import pygame
from config import CELL_SIZE, BLUE
from game.maze import is_walkable


class Player:

    def __init__(self):

        self.x = 1
        self.y = 1

    def move(self, direction):

        moves = {
            "UP": (0, -1),
            "DOWN": (0, 1),
            "LEFT": (-1, 0),
            "RIGHT": (1, 0)
        }

        if direction not in moves:
            return

        dx, dy = moves[direction]

        new_x = self.x + dx
        new_y = self.y + dy

        if is_walkable(new_x, new_y):

            self.x = new_x
            self.y = new_y

    def draw(self, screen):

        center_x = self.x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.y * CELL_SIZE + CELL_SIZE // 2

        pygame.draw.circle(
            screen,
            BLUE,
            (center_x, center_y),
            CELL_SIZE // 3
        )