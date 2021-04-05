from collections import deque

neighbours={'T': ['V'], 'WA': ['NT', 'SA'], 'NT': ['WA', 'Q', 'SA'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'SA', 'V'], 'V': ['SA', 'NSW', 'T']}
colors={'WA': ['red'], 'NT': ['red', 'blue', 'green'], 'SA': ['red', 'blue', 'green'], 'Q': ['green'], 'NSW': ['red', 'blue', 'green'], 'V': ['red', 'blue', 'green'], 'T': ['red', 'blue', 'green']}
#neighbours={'WA': ['SA', 'NT'], 'SA': ['WA', 'NT'], 'NT': ['WA', 'SA']}
#colors={'WA': ['red', 'green', 'blue'], 'SA': ['red', 'green'], 'NT': ['green']}

#Ex. 3
#neighbours={'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'T'], 'SA': ['WA', 'NT', 'V'], 'T': ['NT', 'V'], 'V': ['SA', 'T']}
#colors={'WA': ['red'], 'NT': ['red', 'green'], 'SA': ['red', 'blue', 'green'], 'T': ['red', 'blue', 'green'], 'V': ['red', 'blue']}
states=list(colors.keys())

queue=deque()

for aKey in neighbours.keys():
    for aValue in neighbours[aKey]:
        tpl=(aKey, aValue)
        queue.append(tpl)

def addNeighboursInQueue(dict, key, queue):
    for aKey in dict.keys():
        if aKey==key:
            for i in dict[aKey]:
                tpl=(i, key)
                queue.append(tpl)

while len(queue)>0:
    state1, state2 = queue.popleft()

    if len(colors[state1])>1 and len(colors[state2])==1:
        if colors[state2][0] in colors[state1]:
            colors[state1].remove(colors[state2][0])
            addNeighboursInQueue(neighbours, state1, queue)

def different_colors_constraint(state1, state2):
    if colors[state1]==colors[state2] and state1 in neighbours[state2]:
        return False
    else:
        return True

def more_colors_constraint(state):
    if len(colors[state]) != 1:
        return False
    else:
        return True

def validate_map_coloring(neighbours, colors):
    same_color=[]
    more_colors=[]
    for i in range(len(states)-1):
        for j in range(i+1, len(states)):
            if different_colors_constraint(states[i], states[j])==False:
                same_color.append((states[i], states[j]))
    for i in states:
        if more_colors_constraint(i)==False:
            more_colors.append(i)
    if len(same_color)>0:
        print("States that have the same color: ", same_color)
    if len(more_colors)>0:
        print("States that have more colors: ", more_colors)
    if len(same_color) > 0 or len(more_colors) > 0:
        print("Inconsistenta")
    if len(same_color)==0 and len(more_colors)==0:
        print("Map can be correctly colored!")
        print(colors)

validate_map_coloring(neighbours, colors)
print(colors)