import pygame
from checkers.constants import RED, GREEN, WHITE, BLACK, BLUE, SQUARE_SIZE, display_message
from checkers.game import Game
from minimax.algorithm import minimax

WIN = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Dame")

#FPS=60

turn=GREEN #alegem cine incepe jocul: RED=calculator, GREEN=utilizator

def get_row_col_from_mouse(pos):
    x, y = pos
    row=int(y//SQUARE_SIZE)
    col=int(x//SQUARE_SIZE)
    return row, col

def main():
    run = True
    #clock = pygame.time.Clock()
    game = Game(turn) #initializarea jocului, cu precizarea jucatorului care incepe

    while run:
        #clock.tick(FPS)

        if game.turn == RED: #daca e randul calculatorului, apelam algoritmul minimax si facem cea mai buna mutarea
            value, new_board = minimax(game.get_board(), 3, True, game)
            #value memoreza scorul minim/maxim, dupa caz, iar new_board memoreaza starea din care obtinem acel scor
            game.move(new_board) #calculatroul "muta o piesa" a.i. borad-ul sa devina new_board

        if game.winner()!=None: #winner returneaza un castigator
            display_message(WIN, game.winner())
            run=False #jocul se incheie

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row, col=get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()