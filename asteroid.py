from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(
            255, 255, 255), (
            self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            angle_one = pygame.Vector2(self.velocity.rotate(random_angle))
            angle_two = pygame.Vector2(self.velocity.rotate(-random_angle))
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(
                self.position.x, self.position.y, split_radius)
            asteroid2 = Asteroid(
                self.position.x, self.position.y, split_radius)
            asteroid1.velocity = angle_one * 1.2
            asteroid2.velocity = angle_two * 1.2
