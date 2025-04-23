import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        # Always kill the current asteroid
        self.kill()
        
        # If this is a small asteroid, don't spawn new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generate random angles for the new asteroids
        split_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current one
        velocity1 = self.velocity.rotate(split_angle) * 1.2
        velocity2 = self.velocity.rotate(-split_angle) * 1.2
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2