import timeit


goal_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
goal_2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]


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

    # print(first_row, "first_row")
    # print(last_row, "last_row")
    # print(first_column, "first_column")
    # print(last_column, "last_column")
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




def move_wrap_row(current_state, first_row, last_row):
    child = current_state[:]
    empty_tile_pos = child.index(0)
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
        return None,0


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


# function to create a new object (node) using the Node class
def newNode(state,move, parent,cost):
    return Node(state,move,parent,cost)

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

    state, move = move_wrap_row(node.state, first_row, last_row)
    stateSpace.append(newNode(state,move,node, 2))

    # state, move = move_wrap_column(node.state, first_row, last_row)
    # stateSpace.append(newNode(state,move,node, 2))
    # to delete the nodes which are generated from forbidden moves
    stateSpace = [node for node in stateSpace if node.state != None]

    return stateSpace



##Define h1 function as Hamming distance
def h1(current_node,goal_1, goal_2):
    current = current_node.state
    far_goal_1=0
    far_goal_2=0
    for i in range(0,len(current)-1):
        if current[i] != goal_1[i]:
            far_goal_1+=1
        if current[i] != goal_2[i]:
            far_goal_2+=1
    current_node.h = min(far_goal_1,far_goal_2)

#Define h2 function as sum of permutations
def h2(current_node, goal_1, goal_2):
    current = current_node.state
    far_goal_1=0
    far_goal_2=0
    for i in range(0,len(current)-1):
        for j in range(0,len(current)-1):
            if (current[j]<current[i]) and (current[j]!=0) and (current[i]!=0) and (i<j):
                far_goal_1+=1
    if (current != goal_1) and (far_goal_1 == 0):
        far_goal_1 = 1
    for i in range(0,len(current)-1):
        for j in range(i+1,len(current)-1):
            for k in range(0,len(current)-1):
                if (current[j] == goal_2[k]) and (current[j]!=0) and (goal_2[k]!=0):
                    if j>k:
                        far_goal_2+=1
    current_node.h = min(far_goal_1,far_goal_2)




# define f function: f = h + g
def f(current_node):
    current_node.f = current_node.h + current_node.cost


def aStar(initial_state, g1, g2,h):

    start_node=newNode(initial_state,0,None,0)
    #start_node.h(start_node)
    #start_node.f(start_node)
    h(start_node,goal_1, goal_2)
    f(start_node)
    openList=[]
    solutionPath=[]
    closed=[]
    openList.append(start_node)
    current=openList.pop(0)
    closed.append(current)
    while (timeit.default_timer() - start <= 5000):
        if current.state==g1 or current.state==g2:
            while(current.parent!=None):
                solutionPath.insert(0,current)
                current=current.parent
            solutionPath.insert(0,start_node)
            return solutionPath, closed
        temp=generateSuccessors(current)
        for item in temp:
            h(item, goal_1, goal_2)
            #item.f+=current.f # calculate the cost from the root to the current state
            #item.h+= item.cost
            item.cost+=current.cost
            #item.h+=current.h

            bool = False
            if len(openList) != 0:
                for i in openList:
                    if item.state == i.state:
                        bool = True
                        #  print(item.cost, i.cost)
                        # print(item.state, i.state)
                        if item.cost < i.cost:
                            i.cost = item.cost
                            i.parent = item.parent
                            #i.f = item.f
                            #print(i.cost, "new cost")
            if bool == False:
                openList.append(item)
              #print(item.cost, "cost")
            #print(item.state, item.cost)#########
            f(item)
            #openList.append(item)
        openList.sort(key =lambda x: x.f)
        #for k in openList:
        #    print(k.state, k.cost,k.h,k.f)
        current=openList.pop(0)
        closed.append(current)
        #print(current.state, "pop")################
#while(current.parent!=None):
#    solutionPath.insert(0,current.h)
#    current=current.parent

    return None, None


# Create the soltion files
def createSolutionFile(result, ctr, algName, execution_time, h):
    #name the file
    if h == None:
        fileName = (str(ctr) + "_" + algName + "_solution.txt")
    else:
        fileName = (str(ctr) + "_" + algName + "-" + h +"_solution.txt")
    output = open(fileName,"wt")
    k = 0
    totalCost = 0
    if result == None:
        output.write("No solution found")
    else:
        #for each node in the solution-path print the moved element, the cost, the state of the node
        for i in result:
           output.write(str(i.move))
           output.write(" ")
           if algName== "gbsf":
               output.write(str(i.cost))
               totalCost+=i.cost
           else:
               output.write(str(i.cost - k))
               totalCost+=i.cost-k
           output.write(" ")
           for j in i.state:
               output.write(str(j))
               output.write(" ")
           output.write("\n")
           k = i.cost
        #print total cost
        output.write(str(totalCost))
        output.write(" ")
        #print excecution time
        output.write(str(execution_time))

########################################## For Analysis ######################################
        if algName == 'ucs':
            global tot_cost_ucf
            tot_cost_ucf += totalCost
            global tot_time_ucf
            tot_time_ucf += execution_time
        elif (algName == 'gbsf') and (h == 'h1'):
            global tot_cost_gbfs_h1
            tot_cost_gbfs_h1 += totalCost
            global tot_time_gbfs_h1
            tot_time_gbfs_h1 +=execution_time
        elif (algName == 'gbsf') and (h == 'h2'):
            global tot_cost_gbfs_h2
            tot_cost_gbfs_h2 += totalCost
            global tot_time_gbfs_h2
            tot_time_gbfs_h2 +=execution_time
        elif (algName == 'astar') and (h == 'h1'):
            global tot_cost_astar_h1
            tot_cost_astar_h1 += totalCost
            global tot_time_astar_h1
            tot_time_astar_h1 +=execution_time
        elif (algName == 'astar') and (h == 'h2'):
            global tot_cost_astar_h2
            tot_cost_astar_h2 += totalCost
            global tot_time_astar_h2
            tot_time_astar_h2 +=execution_time
#############################################################################################

# Create the search files
def createSearchFile(closed, ctr, algName, execution_time, h):
    #name the file
    if h == None:
        fileName = (str(ctr) + "_" + algName + "_search.txt")
    else:
        fileName = (str(ctr) + "_" + algName + "-" + h +"_search.txt")
    output = open(fileName,"wt")
    if result == None:
        output.write("No solution found")
    else:
        #for each node in the closed list, print f, g, h, and the state of the node
        for i in closed:
            output.write(str(i.f))
            output.write(" ")
            output.write(str(i.cost))
            output.write(" ")
            output.write(str(i.h))
            output.write(" ")
            for j in i.state:
                output.write(str(j))
                output.write(" ")
            output.write("\n")

# A function to stop the excecution time and call the functions to create the solution and search files
def giveOutput (result, closed, ctr, algName, h):
        #stop the time
        stop = timeit.default_timer()
        #execution time is the difference between start time and stop time
        execution_time = stop - start
        createSolutionFile(result, ctr, algName, execution_time, h)
        createSearchFile(closed, ctr, algName, execution_time, h)
        #elif result == [None]:
        #    print( "Start node was the goal!")
        print("Program Executed in "+str(execution_time))#############



################################################################    Main    #########################################################


initial_state  = []
print("Start computing ...")
fh = open("sample.txt", "r")
counter = 0

#read the sample file line by line
for line in fh.readlines():
    line = line.strip()
    line = line.split(" ")
    for word in line:
        initial_state.append(int(word))
    # defining the # of rows and finding the # of column
    rows= 2
    column = int(len(initial_state)/rows)
    #call boundaries function
    #call boundaries function
    first_row, last_row, first_column, last_column = boundaries(initial_state, rows, column)

    #save the starting time
    start = timeit.default_timer()
    #Call aStar for h1
    result, closed = aStar(initial_state, goal_1, goal_2, h1)

    #create the solution and search files
    giveOutput (result, closed, counter, "astar", 'h1')

    #save the starting time
    start = timeit.default_timer()
    #Call aStar for h2
    result, closed = aStar(initial_state, goal_1, goal_2, h2)


    #create the solution and search files
    giveOutput (result, closed, counter, "astar", 'h2')

    counter += 1
    #reset the initial state
    initial_state  = []
