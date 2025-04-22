import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Initialize the sprite first
        super().__init__()
        
        # Handle group assignment if containers exist
        if hasattr(self, "containers"):
            self.add(self.containers["updatable"])
            self.add(self.containers["drawable"])

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass