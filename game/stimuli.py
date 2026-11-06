import pygame

TARGETS = {
    "UP": (650, 200, 180, 60),
    "DOWN": (650, 280, 180, 60),
    "LEFT": (650, 360, 180, 60),
    "RIGHT": (650, 440, 180, 60)
}


def draw_targets(screen):

    font = pygame.font.SysFont(None, 28)

    for direction, rect in TARGETS.items():

        pygame.draw.rect(
            screen,
            (70, 90, 140),
            rect,
            border_radius=10
        )

        text = font.render(
            direction,
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(
                rect[0] + rect[2] // 2,
                rect[1] + rect[3] // 2
            )
        )

        screen.blit(text, text_rect)