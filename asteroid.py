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
            
        # Generate random angles for the new asteroids
        split_angle = random.uniform(20, 50)
        
        # Create two new asteroids with random radii and velocities
        for _ in range(2):
            # Generate a random radius between min radius and parent size
            min_size = ASTEROID_MIN_RADIUS
            max_size = self.radius - 5  # At least 5 units smaller than parent
            if max_size <= min_size:
                max_size = min_size + 1
                
            new_radius = random.uniform(min_size, max_size)
            
            # Randomize the speed factor for more variety
            from constants import ASTEROID_MIN_SPEED_FACTOR, ASTEROID_MAX_SPEED_FACTOR
            speed_factor = random.uniform(ASTEROID_MIN_SPEED_FACTOR, ASTEROID_MAX_SPEED_FACTOR)
            
            # Create new velocity by rotating the original
            angle = split_angle if _ == 0 else -split_angle
            new_velocity = self.velocity.rotate(angle) * speed_factor
            
            # Add some random variation to make movement more unpredictable
            variation = random.uniform(-20, 20)
            new_velocity = new_velocity.rotate(variation)
            
            # Create the new asteroid
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_velocity
        
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