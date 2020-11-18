from main import goal_1
from main import goal_2

#Define h0 function to use in demo
def h0(current_node,goal_1, goal_2):
    current = current_node.state
    far=0
    empty_tile_pos = current.index(0)
    if empty_tile_pos != 7:
        far = 1
    current_node.h = far

#Define h1 function as Hamming distance
def h1(current_node,goal_1, goal_2):
    current = current_node.state
    far_goal_1=0
    far_goal_2=0
    for i in range(0,7):
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
    for i in range(0,7):
        for j in range(0,7):
            if (current[j]<current[i]) and (current[j]!=0) and (current[i]!=0) and (i<j):
                far_goal_1+=1
    if (current != goal_1) and (far_goal_1 == 0):
        far_goal_1 = 1
    for i in range(0,7):
        for j in range(i+1,7):
            for k in range(0,7):
                if current[j] == goal_2[k] and current[j]!=0 and goal_2[k]!=0:
                    if j>k:
                        far_goal_2+=1
    current_node.h = min(far_goal_1,far_goal_2)


#Define h3 function increment 2 for each number is not in its original row
def h3(current_node, goal_1, goal_2):
    current = current_node.state
    far_goal_1=0
    far_goal_2=0
    for i in range(0,rows):
        for j in range(0,column):
            bool = False
            for k in range(0,column):
                if current[j] == goal_1[k]:
                    bool = True
            if bool == False:
                far_goal_1+= 2
    for i in range(0,rows):
        for j in range(0,column):
            bool = False
            for k in range(0,column):
                if current[j] == goal_2[k]:
                    bool = True
            if bool == False:
                far_goal_2+= 2
    current_node.h = min(far_goal_1,far_goal_2)

# define f function: f = h + g
def f(current_node):
    current_node.f = current_node.h + current_node.cost
