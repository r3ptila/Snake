import pygame

SNAKE_SIZE = 20
WIDTH, HEIGHT = 640, 480

class Snake:
    def __init__(self):
        # Initialize the snake's properties
        self.positions = [(100, 50), (90, 50), (80, 50)]  # Initial positions (x, y)
        self.direction = 'RIGHT'  # Initial direction
        self.score = 0

    def move(self, food):
        # Get the current head position
        head_x, head_y = self.positions[0]

        # Determine the new head position based on the current direction
        if self.direction == 'UP':
            new_head = (head_x, head_y - SNAKE_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + SNAKE_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head_x - SNAKE_SIZE, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + SNAKE_SIZE, head_y)
            
        new_head_x = new_head[0] % WIDTH
        new_head_y = new_head[1] % HEIGHT
        
        new_head = (new_head_x, new_head_y)

        # Insert the new head position at the beginning of the positions list
        self.positions.insert(0, new_head)

        # Check if the snake's head collides with the food
        if  (
            food.position[0] <= self.positions[0][0] <= food.position[0] + SNAKE_SIZE and
            food.position[1] <= self.positions[0][1] <= food.position[1] + SNAKE_SIZE
            ):
            self.score += 1 
            self.extend()     
            food.position = food.spawn_food()
        else:
            # Remove the last segment of the snake to keep it the same length
            self.positions.pop()

    def change_direction(self, new_direction):
        # Change the snake's direction if it's not moving in the opposite direction
        if new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def check_collision(self):
        # Check if the snake's head collides with its body (excluding the head)
        if self.positions[0] in self.positions[1:]:
            return True

    def eat(self, food):
        food_x, food_y = food.position
        head_x, head_y = self.positions[0]

        # Check if the snake's head collides with the food
        if (
            food_x == head_x and
            food_y == head_y
            ):
            self.score += 1
            return True
        return False


    def extend(self):
        # Get the last segment of the snake's body
        tail = self.positions[-1]
        
        # Determine the position of the new segment based on the direction of the tail
        if self.direction == 'UP':
            new_segment = (tail[0], tail[1] + SNAKE_SIZE)
        elif self.direction == 'DOWN':
            new_segment = (tail[0], tail[1] - SNAKE_SIZE)
        elif self.direction == 'LEFT':
            new_segment = (tail[0] + SNAKE_SIZE, tail[1])
        elif self.direction == 'RIGHT':
            new_segment = (tail[0] - SNAKE_SIZE, tail[1])
        
        # Add the new segment to the snake's body
        self.positions.append(new_segment)

    def draw(self, screen):
        # Define the color and size of the snake's body segments
        body_color = (0, 255, 0)  # Green color
        segment_size = SNAKE_SIZE

        # Loop through each segment of the snake's body and draw it
        for segment in self.positions:
            pygame.draw.rect(screen, body_color, (segment[0], segment[1], segment_size, segment_size))

        # Draw the snake's head differently 
        head_color = (0, 0, 255)  # Blue color for the head
        head_x, head_y = self.positions[0]
        pygame.draw.rect(screen, head_color, (head_x, head_y, segment_size, segment_size))