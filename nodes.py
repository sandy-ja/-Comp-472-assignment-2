# Node data structure
class Node:
    def __init__(self, state,move , parent,cost):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the path cost of this node from depth 0.
        self.cost = cost
        # Contains the move that parent node did to get to the new node
        self.move = move
        self.h=0
        self.f=0


#function to get the boundaries of the puzzle as indexes
def boundaries(initial, rows , column):
    first_row = []
    i = 0
    while(i<column):
        first_row.append(int(i))
        i+=1

    last_row = []
    i = len(initial)-column
    while(i<len(initial)):
        last_row.append(int(i))
        i+=1

    i = 0
    first_column = []
    while(i<=len(initial)-1):
        first_column.append(int(i))
        i+=column

    last_column = []
    j=column-1
    while(j<=len(initial)-1):
        last_column.append(int(j))
        j+=column

    return first_row, last_row, first_column, last_column



def move_right(current_state, last_column):
    #make an object copy
    child = current_state[:]
    #find the empty tile position and save it
    empty_tile_pos = child.index(0)
    #check if the empty tile can move right
    if empty_tile_pos not in last_column:
        #swap the values
        temp = child[empty_tile_pos + 1]
        child[empty_tile_pos + 1] = child[empty_tile_pos]
        child[empty_tile_pos]= temp

        cost = 1
        return child, temp
    else:
        #if cannot move, return nothing
        return None,0



def move_left(current_state, first_column):
    #make an object copy
    child = current_state[:]
    #find the empty tile position and save it
    empty_tile_pos = child.index(0)
    #check if empty tile can move left
    if empty_tile_pos not in first_column:
        #swap the values
        temp = child[empty_tile_pos - 1]
        child[empty_tile_pos - 1] = child[empty_tile_pos]
        child[empty_tile_pos]= temp
        cost = 1

        return child, temp
    else:
        #if cannot move, return nothing
        return None,0



def move_up(current_state, first_row):
    #make an object copy
    child = current_state[:]
    #find the empty tile position and save it
    empty_tile_pos = child.index(0)
    #check if empty tile can move up
    if empty_tile_pos not in first_row:
        #swap the values
        temp = child[empty_tile_pos - column]
        child[empty_tile_pos-column] = child[empty_tile_pos]
        child[empty_tile_pos]= temp
        cost = 1
        return child, temp
    else:
        #if cannot move, return nothing
        return None,0

#move the empty tile down and return a new state
def move_down(current_state, last_row):
    #make an object copy
    child = current_state[:]
    #find the empty tile position and save it
    empty_tile_pos = child.index(0)
    #check if empty tile can move down
    if empty_tile_pos not in last_row:
        #swap the values
        temp = child[empty_tile_pos + column]
        child[empty_tile_pos + column] = child[empty_tile_pos]
        child[empty_tile_pos] = temp
        cost = 1
        return child, temp

    else:
        #if cannot move, return nothing
        return None,0


def move_L_Diagonal(current_state, first_row, last_row):
    #make an object copy
    child = current_state[:]
    #find the empty tile position and save it
    empty_tile_pos = child.index(0)
    cost = 3
    #check if the empty tile is in one of the corners and swap the corresponding value
    if empty_tile_pos == first_row[0] or empty_tile_pos == last_row[-1]:
        temp = child[0]
        child[0] = child[-1]
        child[-1] = temp
        if empty_tile_pos == 0:
            return child, child[0]
        else:
            return child, child[-1]

    elif empty_tile_pos == first_row[-1] or empty_tile_pos == last_row[0]:
        temp = child[first_row[-1]]
        child[first_row[-1]] = child[last_row[0]]
        child[last_row[0]] = temp
        if empty_tile_pos == first_row[-1]:
            return child, child[first_row[-1]]
        else:
            return child, child[last_row[0]]
    else:
        #if cannot move, return nothing
        return None,0



def move_S_Diagonal(current_state, first_row, last_row):
    #make an object copy
    child = current_state[:]
    #find the empty tile position and save it
    empty_tile_pos = child.index(0)
    cost = 3
    #check if the empty tile is in one of the corners and swap the corresponding value
    if empty_tile_pos == 0:
        temp = child[0]
        child[0] = child[column+1]
        child[column+1] = temp
        return child, child[0]

    elif empty_tile_pos == first_row[-1]:
        temp = child[first_row[-1]]
        child[first_row[-1]] = child[first_row[-1]+column-1]
        child[first_row[-1]+column+-1] = temp
        return child, child[first_row[-1]]

    elif empty_tile_pos == last_row[0]:
        temp = child[last_row[0]]
        child[last_row[0]] = child[last_row[0]-column+1]
        child[last_row[0]-column+1] = temp
        return child,  child[last_row[0]]

    elif empty_tile_pos == last_row[-1]:
        temp = child[last_row[-1]]
        child[last_row[-1]] = child[last_row[-1]-column-1]
        child[last_row[-1]-column-1] = temp
        return child, child[last_row[-1]]

    else:
        #if cannot move, return nothing
        return None,0



def move_wrap(current_state, first_row, last_row):
    #make an object copy
    child = current_state[:]
    #find the empty tile position and save it
    empty_tile_pos = child.index(0)
    #check if the empty tile is in one of the corners and swap the corresponding value
    if empty_tile_pos == first_row[0] or empty_tile_pos == first_row[-1]:
        cost = 2
        temp = child[first_row[0]]
        child[first_row[0]] = child[first_row[-1]]
        child[first_row[-1]] = temp
        if empty_tile_pos == first_row[0]:
            return child, child[first_row[0]]
        else:
            return child, child[first_row[-1]]

    elif empty_tile_pos == last_row[0] or empty_tile_pos == last_row[-1]:
        cost = 2
        temp = child[last_row[0]]
        child[last_row[0]] = child[last_row[-1]]
        child[last_row[-1]] = temp
        if empty_tile_pos == last_row[0]:
            return child, child[last_row[0]]
        else:
            return child, child[last_row[-1]]
    else:
        #if cannot move, return nothing
        return None,0
