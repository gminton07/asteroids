import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SCORE_DESTROY
from logger import log_state, log_event
from player import Player
from shot import Shot

def main():
    print(f'Starting Asteroids with pygame version: {pygame.version.ver}')
    print('Screen width: {0}'.format(SCREEN_WIDTH))
    print('Screen height: {}'.format(SCREEN_HEIGHT))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    # Create player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    player_score: int = 0

    # Create asteroid field object
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            else:
                pass

        screen.fill('black')

        # Update sprite groups
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print('Game over!\n')
                print('Results:')
                print(f'Time survived: {pygame.time.get_ticks()/1000} sec')
                print(f'Final score: {player_score}')
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    player_score += PLAYER_SCORE_DESTROY

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
