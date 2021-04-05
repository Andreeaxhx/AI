import pygame
from checkers.constants import BLACK, WHITE, RED, GREEN, WIDTH, HEIGHT, SQUARE_SIZE
from checkers.piece import Piece

class Board:
    def __init__(self): #starea initiala
        self.board=[]
        self.create_board()

    def create_board(self):
        self.red_positions = [(0, 0), (0, 1), (0, 2), (0, 3)]
        self.green_positions = [(3, 0), (3, 1), (3, 2), (3, 3)]
        for row in range(4):
            self.board.append([])
            for col in range(4):
                if row == 0:
                    self.board[row].append(Piece(row, col, RED))
                elif row == 3:
                    self.board[row].append(Piece(row, col, GREEN))
                else:
                    self.board[row].append(0)

    def evaluate(self): #functia de evaluare euristica
        #red-green
        sum_red_avans=self.avans(RED)
        sum_green_avans=self.avans(GREEN)
        return sum_red_avans-sum_green_avans

    def avans(self, color):
        head_start=0
        if color==RED:
            for position in self.red_positions:
                head_start+=position[0]

        elif color==GREEN:
            for position in self.green_positions:
                head_start+=(3-position[0])
        return head_start

    def get_all_pieces(self, color): #returneaza o lista cu toate piesele de acea culoare
        pieces=[]
        for row in self.board:
            for piece in row:
                if piece!=0 and piece.color==color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        #se actualizeaza pozitiile pieselor pe tabla
        if piece.color == RED:
            for i in range(0, len(self.red_positions)):
                if self.red_positions[i] == (piece.row, piece.col):
                    self.red_positions[i] = (row, col)
        if piece.color == GREEN:
            for i in range(0, len(self.green_positions)):
                if self.green_positions[i][0] == piece.row and self.green_positions[i][1] == piece.col:
                    self.green_positions[i] = (row, col)

        self.board[piece.row][piece.col], self.board[row][col]=self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def winner(self): #verificarea starii finale
        if self.avans(RED)==12:
            return RED
        if self.avans(GREEN)==12:
            return GREEN
        if self.no_more_valid_moves(RED) and self.avans(RED) > self.avans(GREEN):
            return RED
        if self.no_more_valid_moves(RED) and self.avans(RED) < self.avans(GREEN):
            return GREEN
        if self.no_more_valid_moves(GREEN) and self.avans(RED) > self.avans(GREEN):
            return RED
        if self.no_more_valid_moves(GREEN) and self.avans(RED) < self.avans(GREEN):
            return GREEN
        return None

    def no_more_valid_moves(self, color):
        OK=1
        for piece in self.get_all_pieces(color):
            if self.get_valid_moves(piece)!=[]:
                OK=0
        if OK==1:
            return True
        return False

    def get_valid_moves(self, piece): #generarea mutarilor
        moves=[]
        left=piece.col-1
        right=piece.col+1
        up=piece.row-1
        down=piece.row+1

        if left>=0 and self.board[piece.row][left]==0:
            moves.append((piece.row, left))
        if right<4 and self.board[piece.row][right]==0:
            moves.append((piece.row, right))
        if up>=0 and self.board[up][piece.col]==0:
            moves.append((up, piece.col))
        if down<4 and self.board[down][piece.col]==0:
            moves.append((down, piece.col))

        if left>=0 and up>=0 and self.board[up][left]==0:
            moves.append((up, left))
        if right<4 and up>=0 and self.board[up][right]==0:
            moves.append((up, right))
        if left >= 0 and down<4 and self.board[down][left] == 0:
            moves.append((down, left))
        if right < 4 and down<4 and self.board[down][right] == 0:
            moves.append((down, right))

        return moves

    def draw_cubes(self, window):
        window.fill(BLACK)
        for row in range(4):
            for col in range(row%2, 4, 2):
                pygame.draw.rect(window, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_piece(self, row, col):  # (row, col) a unei piese
        return self.board[row][col]



    def draw(self, window):
        self.draw_cubes(window)
        for row in range(4):
            for col in range(4):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)
