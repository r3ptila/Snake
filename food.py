import pygame
import random
from snake import SNAKE_SIZE

class Food:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.food_image = pygame.image.load("assets/food.png")  # Load the food image
        self.position = self.spawn_food()

    def spawn_food(self):
        # Generate random coordinates for the food within the game boundaries
        x = random.randint(0, self.WIDTH - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE
        y = random.randint(0, self.HEIGHT - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE
        return (x, y)

    def draw(self, screen):
        # Draw the food image at its position
        screen.blit(self.food_image, self.position)
