from copy import deepcopy
from checkers.constants import RED, GREEN

def minimax(current_board, depth, maximize, game):
#position=board, depth=depth of the minimax, maximize=true/false, game=game object
    if depth==0 or current_board.winner()!=None:
        return current_board.evaluate(), current_board

    if maximize: #daca suntem pe un nivel pe care vrem sa maximizam scorul (player=calculator)
        maxEval=float('-inf')
        best_move = None
        for move in get_all_moves(current_board, RED, game):
            #pentru fiecare stare in care se poate ajunge din starea curenta, atunci cand e randul calculatorului
            evaluation=minimax(move, depth-1, False, game)[0]
            #se calculeaza scorul maxim pe care il poate obtine calculatorul, avand in vedere situatia de pe nivelul inverior al arborelui
            maxEval=max(maxEval, evaluation)
            if maxEval==evaluation:
                best_move=move
        #pe langa scorul minim/maxim, functia returneaza si starea care ar trebui aleasa pentru a obtine acel scor
        return maxEval, best_move
    else: #userul va vrea sa minimizeze scorul, asa ca aici se calculeaza scorul minim ce se poate obtine,
          #avand in vedere alegerile pe care le-ar putea face calculatorul
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(current_board, GREEN, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulate_move(piece, move, board, game):
    board.move(piece, move[0], move[1])
    return board

def get_all_moves(board, color, game):
    moves=[] #lista cuprinzand posibile stari (boards) in care se poate ajunge din starea curenta

    for piece in board.get_all_pieces(color):
        valid_moves=board.get_valid_moves(piece) #pentru fiecare piesa de pe tabla se cauta pozitiile pe care se poate muta
        for move in valid_moves: #si pentru fiecare mutare valida
            #valid_moves e o lista cu tuple (row, col)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game) #se simuleaza pe o copie acea mutare
            moves.append(new_board)
    return moves


