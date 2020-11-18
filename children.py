import nodes
# function to create a new object (node) using the Node class
def newNode(state,move, parent,cost):
    return nodes.Node(state,move,parent,cost)

# function to generate the generate children and return them as a list of nodes
def generateSuccessors(node):
    stateSpace = []
    state, move = move_up(node.state, first_row)
    stateSpace.append(newNode(state,move,node, 1))

    state, move = move_down(node.state, last_row)
    stateSpace.append(newNode(state,move,node, 1))

    state, move = move_left(node.state, first_column)
    stateSpace.append(newNode(state,move,node, 1))

    state, move = move_right(node.state, last_column)
    stateSpace.append(newNode(state,move,node, 1))

    state, move = move_L_Diagonal(node.state, first_row, last_row)
    stateSpace.append(newNode(state,move,node, 3))


    state, move = move_S_Diagonal(node.state, first_row, last_row)
    stateSpace.append(newNode(state,move,node, 3))

    state, move = move_wrap(node.state, first_row, last_row)
    stateSpace.append(newNode(state,move,node, 2))
    # to delete the nodes which are generated from forbidden moves
    stateSpace = [node for node in stateSpace if node.state != None]

    return stateSpace
