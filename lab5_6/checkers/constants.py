import pygame

WIDTH=400
HEIGHT=400

SQUARE_SIZE=WIDTH/4

RED=(255, 0, 0)
GREEN=(76, 153, 0)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)
GREY=(128, 128, 128)

def display_message(window, color):
    pygame.time.delay(100)
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    if color == RED:
        text = font.render('Calculatorul a castigat!', True, WHITE, RED)
    elif color == GREEN:
        text = font.render('Utilizatorul a castigat!', True, WHITE, GREEN)
    textRect = text.get_rect()
    textRect.center = (400 // 2, 400 // 2)
    while True:
        window.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
