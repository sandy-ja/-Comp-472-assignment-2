import children
import nodes
import heuristic
# Unifrom cost search method
def uniform_cost(initial_state, g1, g2):
        #make a new node with a state equals to the initial state
        start_node=children.newNode(initial_state,0,None,0)
        openList=[]
        solutionPath=[]
        closed=[]
        #append the start node to the open list
        openList.append(start_node)
        current=openList.pop(0)
        closed.append(current)
        #check if the current state equals one of the two goals, if not, generate the successors until you find one equals to one of the goals
        while (timeit.default_timer() - start <= 10):
            if current.state==g1 or current.state==g2:
                while(current.parent!=None):
                    solutionPath.insert(0,current)
                    current=current.parent
                solutionPath.insert(0,start_node)
                return solutionPath, closed
            #generate the successors
            temp=children.generateSuccessors(current)
            for item in temp:
                # calculate the cost from the root to the current state
                item.cost+=current.cost
                bool = False
                if len(openList) != 0:
                    for i in openList:
                        #check if the open list has the same new item before appending and if it has not the same cost, keep the one with a lower cost
                        if item.state == i.state:
                            bool = True
                            if item.cost < i.cost:
                                i.cost = item.cost
                                i.parent = item.parent
                if bool == False:
                    #append the node to the open list
                    openList.append(item)
            openList.sort(key =lambda x: x.cost)
            #for k in openList:####################
            #    print(k.state, k.cost)
            current=openList.pop(0)
            #append current node to the closed list
            closed.append(current)
        return None,None


def Greedy_Best_First(initial_state, g1, g2, h):
    #make a new node with a state equals to the initial state
    start_node = children.newNode(initial_state,0, None, 0)
    h(start_node, goal_1, goal_2)
    openList = []
    solutionPath = []
    closed=[]
    #append the start node to the open list
    openList.append(start_node)
    current = openList.pop(0)
    closed.append(current)
    #check if the current state equals one of the two goals, if not, generate the successors until you find one equals to one of the goals
    while (timeit.default_timer() - start <= 60):
        if current.state==g1 or current.state==g2:
            while(current.parent != None):
                 solutionPath.insert(0,current)
                 current = current.parent

            solutionPath.insert(0,start_node)
            return solutionPath, closed
        #generate the successors
        temp=children.generateSuccessors(current)
        #openList.extend(generateSuccessors(current))
        #apply the heuristic function on each node
        for item in temp:
            h(item, goal_1, goal_2)
            #append the node to the open list
            openList.append(item)
        openList.sort(key = lambda x: x.h)
        #for k in openList:
        #    print(k.state, k.cost, k.h)
        #pop the first element(that has the lowest h) from the queue and make it equal to current
        current = openList.pop(0)
        #append current node to the closed list
        closed.append(current)
        #print(current.state, "pop")################
    #while(current.parent != None):
    #    solutionPath.insert(0,current.h)
    #    current = current.parent
    return None, None



def aStar(initial_state, g1, g2,h):

    start_node=children.newNode(initial_state,0,None,0)
    #start_node.h(start_node)
    #start_node.f(start_node)
    h(start_node, goal_1, goal_2)
    heuristic.f(start_node)
    openList=[]
    solutionPath=[]
    closed=[]
    openList.append(start_node)
    current=openList.pop(0)
    closed.append(current)
    while (timeit.default_timer() - start <= 60):
        if current.state==g1 or current.state==g2:
            while(current.parent!=None):
                solutionPath.insert(0,current)
                current=current.parent
            solutionPath.insert(0,start_node)
            return solutionPath, closed
        temp=children.generateSuccessors(current)
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
            heuristic.f(item)
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
