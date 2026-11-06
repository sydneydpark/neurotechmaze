import pygame
import sys

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    BLACK,
    WHITE,
    GREEN
)

from game.maze import draw_maze, reached_goal
from game.player import Player
from game.stimuli import draw_targets


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("SSVEP BCI Maze Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)


# Create player
player = Player()

running = True
game_won = False


# Keyboard controls
KEY_DIRECTIONS = {
    pygame.K_UP: "UP",
    pygame.K_DOWN: "DOWN",
    pygame.K_LEFT: "LEFT",
    pygame.K_RIGHT: "RIGHT"
}


# Main game loop
while running:

    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r:

                player = Player()
                game_won = False

            if not game_won:

                if event.key in KEY_DIRECTIONS:

                    direction = KEY_DIRECTIONS[event.key]

                    player.move(direction)

    # Check whether player reached goal
    if reached_goal(player.x, player.y):

        game_won = True

    # Background
    screen.fill((35, 35, 45))

    # Draw maze
    draw_maze(screen)

    # Draw player
    player.draw(screen)

    # Draw directional targets
    draw_targets(screen)

    # Instructions
    instructions = font.render(
        "Use arrow keys to move",
        True,
        WHITE
    )

    screen.blit(
        instructions,
        (610, 40)
    )

    # Victory message
    if game_won:

        victory = font.render(
            "YOU WON!",
            True,
            GREEN
        )

        screen.blit(
            victory,
            (610, 100)
        )

        restart = pygame.font.SysFont(
            None, 24
        ).render(
            "Press R to restart",
            True,
            WHITE
        )

        screen.blit(
            restart,
            (610, 135)
        )

    pygame.display.flip()


pygame.quit()
sys.exit()