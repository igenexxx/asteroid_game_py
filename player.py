import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.current_speed = 0
        self.forward_vector = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Decrease the shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
    
        # Handle rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
            
        # Update forward vector based on current rotation
        self.forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Handle acceleration/deceleration
        if keys[pygame.K_w]:
            self.accelerate(dt)
        elif keys[pygame.K_s]:
            self.accelerate(-dt)
        else:
            self.decelerate(dt)
            
        # Apply movement based on current speed
        self.move(dt)
            
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        # Increase speed in the direction of acceleration (positive or negative)
        acceleration_direction = 1 if dt > 0 else -1
        
        # Accelerate based on the sign of dt (positive for forward, negative for backward)
        self.current_speed += PLAYER_ACCELERATION * abs(dt) * acceleration_direction
        
        # Limit the speed to maximum in either direction
        if self.current_speed > PLAYER_MAX_SPEED:
            self.current_speed = PLAYER_MAX_SPEED
        elif self.current_speed < -PLAYER_MAX_SPEED:
            self.current_speed = -PLAYER_MAX_SPEED
            
    def decelerate(self, dt):
        # Slow down when no movement keys are pressed
        if self.current_speed > 0:
            self.current_speed -= PLAYER_DECELERATION * dt
            if self.current_speed < 0:
                self.current_speed = 0
        elif self.current_speed < 0:
            self.current_speed += PLAYER_DECELERATION * dt
            if self.current_speed > 0:
                self.current_speed = 0
                
    def move(self, dt):
        # Move based on current speed and direction
        self.position += self.forward_vector * self.current_speed * dt

    def shoot(self):
        if self.shoot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.shoot_timer = PLAYER_SHOT_COOLDOWN
