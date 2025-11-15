import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, shot):
        self.kill()
        shot.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        first_velocity = self.velocity.rotate(angle)
        second_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_asteroid.velocity = first_velocity * 1.2
        second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_asteroid.velocity = second_velocity
