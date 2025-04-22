import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0


    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, dt):
        # Call rotate method with dt
        self.rotate(dt)

    def move(self, dt):
        # Convert dt from milliseconds to seconds
        dt_seconds = dt / 1000
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt_seconds
    
    def rotate(self, dt):
        keys = pygame.key.get_pressed()
        
        # Convert dt from milliseconds to seconds and use higher rotation speed
        rotation_speed = 300  # degrees per second
        dt_seconds = dt / 1000
        
        if keys[pygame.K_LEFT]:
            self.rotation -= rotation_speed * dt_seconds
        if keys[pygame.K_RIGHT]:
            self.rotation += rotation_speed * dt_seconds
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
