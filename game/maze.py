import pygame
from config import CELL_SIZE, BLACK, WHITE, GREEN

MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def draw_maze(screen):

    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):

            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if MAZE[row][col] == 1:
                color = BLACK

            elif MAZE[row][col] == 2:
                color = GREEN

            else:
                color = WHITE

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

            pygame.draw.rect(
                screen,
                (190, 190, 190),
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )


def is_walkable(x, y):

    if y < 0 or y >= len(MAZE):
        return False

    if x < 0 or x >= len(MAZE[0]):
        return False

    return MAZE[y][x] != 1


def reached_goal(x, y):

    return MAZE[y][x] == 2