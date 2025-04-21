import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        # method to check for collisions. It should take 1 argument (another CircleShape object) and return True or False.
        # Each CircleShape's position property is a pygame.Vector2. Use its distance_to method to calculate the distance between the two shapes.
        distance = self.position.distance_to(other.position)
        sum_radiuses = self.radius + other.radius 
        return distance <= sum_radiuses 
        # After the update step in your game loop, iterate over all of the objects in your asteroids group. Check if any of them collide with the player. If a collision is detected, the program should print Game over! and immediately exit the program.