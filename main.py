import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = { "updatable": updatable, "drawable": drawable}
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # Create player at center of screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        Player.containers["updatable"].update(dt)
        for drawable_object in Player.containers["drawable"]:
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)


if __name__ == "__main__":
    main()