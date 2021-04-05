import random
import sys
from collections import deque

SIZE = (79, 39)

################################################################# CONSTRUCTIA LABIRINTULUI ###########################################################################
if sys.getrecursionlimit() < SIZE[0] * SIZE[1]:
    sys.setrecursionlimit(SIZE[0] * SIZE[1])
# if max recursion limit is lower than needed, adjust it

N, S, E, W = 1, 2, 4, 8
# directions translated into bitnums to store information on all cleared walls in one variable per cell

GO_DIR = {N: (0, -1), S: (0, 1), E: (1, 0), W: (-1, 0)}
# dictionary with directions translated to digging moves

REVERSE = {E: W, W: E, N: S, S: N}
# when a passage is dug from a cell, the other cell obtains the reverse passage, too

lab = list(list(0 for i in range(SIZE[0])) for j in range(SIZE[1]))


# labyrinth is prepared

def dig(x, y):
    # digs passage from a cell (x, y) in an unvisited cell
    dirs = [N, E, W, S]
    random.shuffle(dirs)
    # shuffles directions each time for more randomness
    for dir in dirs:
        new_x = x + GO_DIR[dir][0]
        new_y = y + GO_DIR[dir][1]
        if (new_y in range(SIZE[1])) and \
                (new_x in range(SIZE[0])) and \
                (lab[new_y][new_x] == 0):
            # checks if the new cell is not visited
            lab[y][x] |= dir
            lab[new_y][new_x] |= REVERSE[dir]
            # if so, apply info on passages to both cells
            dig(new_x, new_y)
            # repeat recursively


def check():
    # displays the cells' values for check-up
    for i in range(SIZE[1]):
        for j in range(SIZE[0]):
            print(" " * (1 - (lab[i][j] // 10)) + \
                  str(lab[i][j]), end='|')
        print('')

maze = list()

def draw():
    # displays the labyrinth
    print("3D version: instagram.com/p/BQszVwBhoYT")
    #print("\nLabyrinth of Kuba #" + str(seed) + " (" + str(SIZE[0]) + "x" + str(SIZE[1]) + ")")
    # prints the seed (for reference) and the lab size
    print("_" * (SIZE[0] * 2))
    for j in range(SIZE[1]):
        line = list()
        if j != 0:
            #print("|", end='')
            line.append("|")
        else:
            #print("_", end='')
            line.append("_")
        for i in range(SIZE[0]):
            if (lab[j][i] & S != 0):
                #print(" ", end='')
                line.append(" ")
            else:
                #print("_", end='')
                line.append("_")
            if (lab[j][i] & E != 0):
                if ((lab[j][i] | lab[j][i + 1]) & S != 0):
                   # print(" ", end='')
                    line.append(" ")
                else:
                   # print("_", end='')
                    line.append("_")
            elif (j == SIZE[1] - 1) & (i == SIZE[0] - 1):
                #print("_", end='')
                line.append("_")
            else:
               # print("|", end='')
                line.append("|")
       # print("")
        maze.append(line)
    print("Try 'Labyrinth 2.0' for roguelike xp! ;)")
################################################################# CONSTRUCTIA LABIRINTULUI ###########################################################################


######################################################################### STARILE ###################################################################################

n = SIZE[0]
m = SIZE[1]

seed = 1 #random.randint(0, 1000)
random.seed(seed)
dig(SIZE[0] // 2, SIZE[1] // 2)
draw()
print("_" * n)
for i in range(0,n):
    for j in range(0,m):
        print(maze[i][j], end='')
    print()

x_s = random.randint(0, n)
y_s = random.randint(0, m)
while maze[x_s][y_s]=="|":
    x_s = random.randint(0, n)
    y_s = random.randint(0, m)

x_d=random.randint(0, n)
y_d=random.randint(0, m)
while maze[x_s][y_s]=="|":
    x_d = random.randint(0, n)
    y_d = random.randint(0, m)

x_c = x_s
y_c = y_s

N = 0; S = 0; E = 0; W = 0

def valid_transitions(x, y):
    #return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and (maze[y][x] is " " or maze[y][x] is "_")
    N=0; S=0; E=0; V=0

    if x-1>=0 and maze[x-1][y]==" ":
        N=1
    if x+1<n and maze[x+1][y]==" ":
        S=1
    if y+1<m and (maze[x][y+1]==" " or maze[x+1][y]=="_"):
        E=1
    if y-1>=0 and (maze[x][y-1]==" " or maze[x-1][y]=="_"):
        V=1
    return (N, S, E, V)


#representation of a state
aState=[(n, m), (x_c, y_c), (x_d, y_d), [], (N, S, E, W)]

#initial state
initialState=[(n, m), (x_s, y_s), (x_d, y_d), [], (N, S, E, W)]

def Initialize (n, m, x_s, y_s, x_d, y_d):
    N, S, E, V = valid_transitions(x_s, y_s)
    return list((n, m), (x_s, y_s), (x_d, y_d), [], (N, S, E, V))

#final state
finalState=[(n, m), (x_d, y_d), (x_d, y_d), [], (N, S, E, W)]

def isFinal(aState):
    if aState[1][0]==x_d and aState[1][1]==y_d:
        return True
    else:
        return False

#x=aState[1][0]
#y=aState[1][1]
#N, S, E, W = valid_transitions(x, y)

def Validate(aState, card):
    x = aState[1][0]
    y = aState[1][1]
    if card=="N":
       # if x-1>=0 and maze[x-1][y]==" ":
       if valid_transitions(x, y)[0]==1:
            return True
    elif card=="S":
       # if x+1<n and maze[x+1][y]==" ":
       if valid_transitions(x, y)[1] == 1:
            return True
    elif card=="E":
       # if y+1<m and (maze[x][y+1]==" " or maze[x][y+1]=="_"):
       if valid_transitions(x, y)[2] == 1:
            return True
    elif card=="W":
       # if y-1>=0 and (maze[x][y-1]==" " or maze[x][y-1]=="_"):
       if valid_transitions(x, y)[3] == 1:
            return True


def Transition (aState, card):
    x = aState[1][0]
    y = aState[1][1]
    def GoNorth(x, y):
        y=y-1
        return (x, y)
    def GoSouth(x, y):
        y=y+1
        return (x, y)
    def GoEast(x, y):
        x=x+1
        return (x, y)
    def GoWest(x, y):
        x=x-1
        return (x, y)

    if card == "N" and Validate(aState, card) == True:
        GoNorth(x, y)
    elif card == "S" and Validate(aState, card) == True:
        GoSouth(x, y)
    elif card == "E" and Validate(aState, card) == True:
        GoEast(x, y)
    elif card == "W" and Validate(aState, card) == True:
        GoWest(x, y)

    aState[1]=(x, y)
    N, S, E, W = valid_transitions(x, y)
    aState[4]=(N, S, E, W)
    return aState

######################################################################### STARILE ###################################################################################

def valid(aState): #Backtracking
    x = aState[1][0]
    y = aState[1][1]

    ones = 0
    for nr in aState[4]:
        if nr == 1:
            ones += 1
    return 0 <= x < aState[0][0] and 0 <= y < aState[0][1] and ones > 1

######################################################################## BACKTRACKING ###############################################################################
path = list()
    #aState=[(n, m), (x_c, y_c), (x_d, y_d), [], (N, S, E, W)]

def resolve(aState,path):
        if isFinal(aState) == True:
            return path

        if not valid(aState):
            return None

        #NORTH
        if maze[aState[1][0]-1][aState[1][1]] == " ":
            northState = [(aState[0][0], aState[0][1]), (aState[1][0]-1, aState[1][1]), (aState[2][0], aState[2][1]), aState[3], valid_transitions(aState[1][0]-1, aState[1][1])]
            if resolve(northState,path) is not None:
                path.append('N')
                print('N')
                return path
        # SOUTH
        if maze[aState[1][0] + 1][aState[1][1]] == " ":
            southState = [(aState[0][0], aState[0][1]), (aState[1][0] + 1, aState[1][1]), (aState[2][0], aState[2][1]), aState[3], valid_transitions(aState[1][0]-1, aState[1][1])]
            if resolve(southState,path) is not None:
                path.append('S')
                print('S')
                return path
        # EST
        if maze[aState[1][0]][aState[1][1] + 1] == " " or maze[aState[1][0]][aState[1][1] + 1] == "_":
            estState = [(aState[0][0], aState[0][1]), (aState[1][0] , aState[1][1] + 1), (aState[2][0], aState[2][1]), aState[3], valid_transitions(aState[1][0]-1, aState[1][1])]
            if resolve(estState,path) is not None:
                path.append('E')
                print('E')
                return path
        # WEST
        if maze[aState[1][0]][aState[1][1] - 1] == " " or maze[aState[1][0]][aState[1][1] - 1] == "_":
            westState = [(aState[0][0], aState[0][1]), (aState[1][0], aState[1][1] - 1), (aState[2][0], aState[2][1]), aState[3], valid_transitions(aState[1][0]-1, aState[1][1])]
            if resolve(westState,path) is not None:
                path.append('V')
                print('V')
                return path

        if len(path) > 0:
            path.remove(len(path) - 1)

path = resolve(initialState,path)
print(path)
######################################################################## BACKTRACKING ###############################################################################


########################################################################### BFS #####################################################################################

queue = deque()
finalPath = {}
visited=set()

def BFS(aState):
    x_c, y_c = aState[1]
    queue.append((x_c, y_c))
    finalPath[x_c, y_c] = x_c, y_c

    while len(queue) > 0:
        x_c, y_c = queue.popleft()

        if Validate(aState, "N") and Transition(aState, "N")[1] not in visited:  # cell up
            cell = Transition(aState, "N")[1]
            finalPath[cell] = x_c, y_c

            queue.append(cell)
            visited.add(cell)

        if Validate(aState, "S") and Transition(aState, "S")[1] not in visited:  # down
            cell = Transition(aState, "S")[1]
            finalPath[cell] = x_c, y_c

            queue.append(cell)
            visited.add(cell)
            #print(finalPath)

        if Validate(aState, "E") and Transition(aState, "E")[1] not in visited:  # right
            cell = Transition(aState, "E")[1]
            finalPath[cell] = x_c, y_c

            queue.append(cell)
            visited.add(cell)

        if Validate(aState, "W") and Transition(aState, "W")[1] not in visited:  # up
            cell = Transition(aState, "W")[1]
            finalPath[cell] = x_c, y_c

            queue.append(cell)
            visited.add(cell)
    path_to_return=[]
    path_to_return.append(x_c, y_c)
    while (x_c, y_c) != (x_s, y_s):
        path_to_return.append(finalPath[x_c, y_c])
        x_c, y_c = finalPath[x_c, y_c]

########################################################################### BFS #####################################################################################
