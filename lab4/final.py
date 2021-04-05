#country = {"WA":["SA" ,"NT"],"SA":["WA","NT"],"NT":["WA","SA"]}
#state_colors = {"WA":["red", "green", "blue"],"SA":["red" ,"green"],"NT":["green"]}

#country = {'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'T'], 'SA': ['WA', 'NT', 'V'], 'T': ['NT', 'V'], 'V': ['SA', 'T']}
#state_colors = {'WA': ['red'], 'NT': ['red', 'green'], 'SA': ['red', 'blue', 'green'], 'T': ['red', 'blue', 'green'], 'V': ['red', 'blue']}

country = {"T": ["V"], "WA": ["NT", "SA"], "NT": ["WA", "Q", "SA"], "SA": ["WA", "NT", "Q", "NSW", "V"], "Q": ["NT", "SA", "NSW"], "NSW": ["Q", "SA", "V"], "V": ["SA", "NSW", "T"]}
state_colors = {"T": ["red", "blue", "green"], "WA": ["red"], "NT": ["red", "blue", "green"], "SA": ["red", "blue", "green"], "Q": ["green"], "NSW": ["red", "blue", "green"], "V": ["red", "blue", "green"]}

list_of_states=list(country.keys())
queue = []
inconsistenta=False
same_color=[]

def addNeighboursInQueue(dict, key, queue):
        for aKey in dict.keys():
            if aKey == key:
                for i in dict[aKey]:
                    tpl = (i, key)
                    queue.append(tpl)

def different_colors_constraint(state):
    if len(state_colors[state]) == 0:
        return False
    else:
        return True

def remove_inconsistent_values(state1, state2):
    removed = False
    if len(state_colors[state1]) >= 1 and len(state_colors[state2]) == 1:  # more than 1 colors in a state and the other has exactly one
        for index in range(-1, len(state_colors[state1]) - 1):
            if state_colors[state2][0] == state_colors[state1][index]:  # the color is the same
                state_colors[state1].pop(index)  # domain = domain - that_color
                removed = True
    return removed

def AC_3():
    for key in country:
        for value in country[key]:
            queue.append((key, value))

    while len(queue) != 0:
        state1, state2 = queue.pop(0)  # WA SA
        if remove_inconsistent_values(state1, state2) == True:
            addNeighboursInQueue(country, state1, queue)

AC_3()

no_colors=[]
for i in list_of_states:
    if different_colors_constraint(i)==False:
        no_colors.append(i)
        inconsistenta=True

if inconsistenta==True:
    print("Inconsistenta")
    print("States that have no colors:", no_colors)
    print(state_colors)
else:
    print("Harta se poate colora!")
    print(state_colors)