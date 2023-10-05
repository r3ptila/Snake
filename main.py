import sys
import pygame
from snake import Snake
from food import Food
import game_ui

pygame.init()

WIDTH, HEIGHT = 640, 480

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_color = (30, 30, 30) 

pygame.display.set_caption("Snake")
icon = pygame.image.load("assets/icon.bmp")
pygame.display.set_icon(icon)

snake = Snake()
food = Food(WIDTH, HEIGHT)
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')
    
    snake.move(food)
    
    if snake.check_collision():
        game_over = True
    
    if snake.eat(food):
        snake.extend()
        food.spawn_food()
      
    screen.fill(background_color)
    snake.draw(screen)
    food.draw(screen)
    game_ui.draw_score(screen, snake.score)
    
    pygame.display.update()
    clock.tick(7)
 
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)
    game_ui.show_game_over(screen, snake.score)
    
    pygame.display.update()
    clock.tick(7)