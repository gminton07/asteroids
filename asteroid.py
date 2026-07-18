import pygame
import random

from logger import log_event

from circleshape import CircleShape

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen, color='white'):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event('asteroid_split')
            angle = random.uniform(20.0, 50.0)
            new_vectors = [self.velocity.rotate(angle), self.velocity.rotate(- angle)]
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroids = [Asteroid(self.position.x, self.position.y, new_radius) for _ in range(2)]
            
            for i in range(2):
                new_asteroids[i].velocity = new_vectors[i] * 1.2
