import pygame

def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(text, text_rect)

def show_game_over(screen, score):
    font = pygame.font.Font(None, 72)
    text = font.render(f'Game Over', True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2 - 50)

    font_score = pygame.font.Font(None, 36)
    score_text = font_score.render(f'Your Score: {score}', True, (255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)

    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
