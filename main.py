import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill("black")

        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        # pauses game loop until 1/60th of a second has past.
        # prevents changes in CPU clock speed changing the game speed.
        # returns the time since its last call.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
