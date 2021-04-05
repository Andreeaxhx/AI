import pygame
from checkers.board import Board
from checkers.constants import RED, GREEN, BLUE, SQUARE_SIZE

class Game:
    def __init__(self, turn): #initializarea jocului
        self.board = Board()
        self.turn = turn
        self.valid_moves = []
        self.selected = None
        self.window = pygame.display.set_mode((400, 400))

    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def winner(self):
        return self.board.winner()

    def select(self, row, col): #se selecteaza un rand si o coloana pe care urmeaza sa se mute piesa
        if self.selected: #daca este selectata o piesa
            result=self._move(row, col) #se incearca mutarea piesei acolo unde vrem noi, si totodata este returnat true daca s-a reusit mutarea
            if not result: #daca nu s-a reusit mutarea
                self.selected=None #se "deselecteaza" piesa selectata anterior
                self.select(row, col) #si se selecteaza din nou un rand si o coloana pe care vrem sa mutam piesa
        else:
            piece=self.board.get_piece(row, col)
            if piece!=0 and piece.color==self.turn:
                self.selected=piece
                self.valid_moves=self.board.get_valid_moves(piece)
                return True

        return False

    def _move(self, row, col):
        where_to=self.board.get_piece(row, col) #selectam locul in care vrem sa mutam piesa
        if self.selected and where_to==0 and (row, col) in self.valid_moves:
            #si daca in prealabil am selectat o piesa, locul in care vrem sa o mutam e gol si tototdata
            #locul face parte din mutarile valide, atunci:
            self.board.move(self.selected, row, col) #mutam piesa selectata in casuta selectata
            self.change_turn() #si schimbam tura
        else:
            return False
        return True

    def draw_valid_moves(self, moves): #deseneaza cerculete albastre in locurile in care se poate muta o piesa
        for move in moves:
            row, col=move
            pygame.draw.circle(self.window, BLUE, (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2), 15) #???

    def change_turn(self):
        self.valid_moves=[] #lista cu mutarile valide se reseteaza
        if self.turn==RED:
            self.turn=GREEN
        else:
            self.turn=RED

    def get_board(self):
        return self.board

    def move(self, board):
        #ai move actualizeaza starea jocului cu una care se considera a fi cea mai buna intr-un anumit moment al jocului
        self.board=board
        self.change_turn()

