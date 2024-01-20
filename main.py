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

def main():

    snake = Snake()
    food = Food(WIDTH, HEIGHT)
    game_over = False

    while True:
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        snake.change_direction('UP')
                        pygame.time.delay(75)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        snake.change_direction('DOWN')
                        pygame.time.delay(75)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        snake.change_direction('LEFT')
                        pygame.time.delay(75)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        snake.change_direction('RIGHT')
                        pygame.time.delay(75)
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
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
            clock.tick(6)
        

        while game_over:

            screen.fill(background_color)
            game_ui.show_game_over(screen, snake.score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        main()

            pygame.display.update()
            clock.tick(6)

def main_menu(screen):
    start = False
    while not start:
        game_ui.draw_main_menu(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

main_menu(screen)