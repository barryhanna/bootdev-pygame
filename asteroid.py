from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        screen.draw.circle(pygame.Vector2(
            self.x, self.y), self.radius, width=2)

    def update(self, dt):
        self.x = self.x + (self.velocity * dt)
        self.y = self.y + (self.velocity * dt)
