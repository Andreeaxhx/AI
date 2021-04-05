import random

SIZE=(15, 15)
n=SIZE[0]
m=SIZE[1]

x_s=random.randrange(SIZE[0])
y_s=random.randrange(SIZE[1])
while maze[x_s][y_s]==0:
    x_s = random.randrange()
    y_s = random.randrange()

x_d=random.randrange()
y_d=random.randrange()
while maze[x_s][y_s]==0:
    x_d = random.randrange()
    y_d = random.randrange()

x_c=x_s
y_c=y_s

N = 0; S = 0; E = 0; W = 0
#GO_DIR = {N: (0, -1), S: (0, 1), E: (1, 0), W: (-1, 0)}
def valid_transitions(x, y):
    N=0; S=0; E=0; V=0

    if y-1>=0 and maze[x][y-1]==1:
        N=1
    if y+1<n and maze[x+1][y]==1:
        S=1
    if x+1<m and maze[x+1][y]==1:
        E=1
    if x-1>=0 and maze[x-1][y]==1:
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

x=aState[1][0]
y=aState[1][1]
N, S, E, W = valid_transitions(x, y)

def Validate(aState, card):
    x = aState[1][0]
    y = aState[1][1]
    if card=="N":
        if y-1>=0 and maze[x][y-1]==1:
            return True
    elif card=="S":
        if y+1<n and maze[x][y+1]==1:
            return True
    elif card=="E":
        if x+1<m and maze[x+1][y]==1:
            return True
    elif card=="W":
        if x-1>=0 and maze[x-1][y]==1:
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
    cardinals=["N", "S", "E", "W"]
    random.shuffle(cardinals)

    for i in cardinals:
        if card == i and i == "N" and Validate(aState, i) == True:
            GoNorth(x, y)
        elif card == i and i == "S" and Validate(aState, i) == True:
            GoSouth(x, y)
        elif card == i and i == "E" and Validate(aState, i) == True:
            GoEast(x, y)
        elif card == i and i == "W" and Validate(aState, i) == True:
            GoWest(x, y)

    aState[1]=(x, y)
    N, S, E, W=valid_transitions(x, y)
    aState[4]=(N, S, E, W)
    return aState























