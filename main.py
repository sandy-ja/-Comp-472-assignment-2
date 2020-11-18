import timeit
import nodes
import algorithms
import heuristic
import output
#defining the two goal states
goal_1 = [1, 2, 3, 4, 5, 6, 7, 0]
goal_2 = [1, 3, 5, 7, 2, 4, 6, 0]


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
    first_row, last_row, first_column, last_column = nodes.boundaries(initial_state, rows, column)

    #save the starting time
    start = timeit.default_timer()
    #Call aStar for h1
    result, closed = algorithms.aStar(initial_state, goal_1, goal_2, heuristic.h1)

    # ##################################### For Analysis ####################################
    # if result == None :
    #         Tot_Len_No_Sol_aStar_h1+=1
    # else:
    #     Tot_Len_Sol_aStar_h1 += len(result)
    #     Tot_Len_Sch_aStar_h1 += len(closed)
    #######################################################################################
    #create the solution and search files
    output.giveOutput (result, closed, counter, "astar", 'h1')

    #save the starting time
    start = timeit.default_timer()
    #Call aStar for h2
    result, closed = algorithms.aStar(initial_state, goal_1, goal_2, heuristic.h2)

    ##################################### For Analysis ####################################
    # if result == None :
    #         Tot_Len_No_Sol_aStar_h2+=1
    # else:
    #     Tot_Len_Sol_aStar_h2 += len(result)
    #     Tot_Len_Sch_aStar_h2 += len(closed)
    #######################################################################################
    #create the solution and search files
    output.giveOutput (result, closed, counter, "astar", 'h2')

    #save the starting time
    start = timeit.default_timer()
    #Call Uniform cost
    result, closed = algorithms.uniform_cost(initial_state, goal_1, goal_2)

    ##################################### For Analysis ####################################
    # if result == None :
    #         Tot_Len_No_Sol_Uniform +=1
    # else:
    #     Tot_Len_Sol_Uniform += len(result)
    #     Tot_Len_Sch_Uniform += len(closed)
    #######################################################################################
    #create the solution and search files
    output.giveOutput (result, closed, counter, "ucs", None)



    #save the starting time
    start = timeit.default_timer()
    #Call Greedy_Best_First for h1
    result, closed = algorithms.Greedy_Best_First(initial_state, goal_1, goal_2, heuristic.h1)
    ##################################### For Analysis ####################################
    # if result == None :
    #     Tot_Len_No_Sol_Greedy_Best_First_h1 += 1
    #
    # else:
    #     Tot_Len_Sol_Greedy_Best_First_h1 += len(result)
    #     Tot_Len_Sch_Greedy_Best_First_h1 += len(closed)
    #######################################################################################
    #create the solution and search files
    output.giveOutput (result, closed, counter, "gbsf", 'h1')

    #save the starting time
    start = timeit.default_timer()
    #Call Greedy_Best_First for h2
    result, closed = algorithms.Greedy_Best_First(initial_state, goal_1, goal_2, heuristic.h2)

    ##################################### For Analysis ####################################
    # if result == None :
    #     Tot_Len_No_Sol_Greedy_Best_First_h2 += 1
    #
    # else:
    #     Tot_Len_Sol_Greedy_Best_First_h2 += len(result)
    #     Tot_Len_Sch_Greedy_Best_First_h2 += len(closed)
    #######################################################################################
    #create the solution and search files
    output.giveOutput (result, closed, counter, "gbsf", 'h2')

    counter += 1
    #reset the initial state
    initial_state  = []

     ################################################################ For Analysis ##########################################################
# print("\n")
# print("############################_aStar_h1_##############################\n")
#
# print('Total length solution path aStar_h1: ', Tot_Len_Sol_aStar_h1)
# print('Average length solution path aStar_h1: ',Tot_Len_Sol_aStar_h1/(50-Tot_Len_No_Sol_aStar_h1))
#
# print('Total length search path aStar_h1: ', Tot_Len_Sch_aStar_h1)
# print('Average length search path aStar_h1: ', Tot_Len_Sch_aStar_h1/(50-Tot_Len_No_Sol_aStar_h1))
#
# print('Total Number of No solution aStar_h1: ', Tot_Len_No_Sol_aStar_h1)
# print('Average Number of No solution aStar_h1: ', Tot_Len_No_Sol_aStar_h1/50)
#
# print('Total cost aStar_h1: ', tot_cost_astar_h1)
# print('Average cost aStar_h1: ', tot_cost_astar_h1/(50-Tot_Len_No_Sol_aStar_h1))
#
# print('Total excution time aStar_h1: ', tot_time_astar_h1)
# print('Average excution time aStar_h1: ', tot_time_astar_h1/(50-Tot_Len_No_Sol_aStar_h1))
#
#
# print("\n")
# print("############################_aStar_h2_##############################\n")
#
# print('Total length solution path aStar_h2: ', Tot_Len_Sol_aStar_h2)
# print('Average length solution path aStar_h2: ',Tot_Len_Sol_aStar_h2/(50-Tot_Len_No_Sol_aStar_h2))
#
# print('Total length search path aStar_h2: ', Tot_Len_Sch_aStar_h2)
# print('Average length search path aStar_h2: ', Tot_Len_Sch_aStar_h2/(50-Tot_Len_No_Sol_aStar_h2))
#
# print('Total Number of No solution aStar_h2: ', Tot_Len_No_Sol_aStar_h2)
# print('Average Number of No solution aStar_h2: ', Tot_Len_No_Sol_aStar_h2/50)
#
# print('Total cost aStar_h2: ', tot_cost_astar_h2)
# print('Average cost aStar_h2: ', tot_cost_astar_h2/(50-Tot_Len_No_Sol_aStar_h2))
#
# print('Total excution time aStar_h2: ', tot_time_astar_h2)
# print('Average excution time aStar_h2: ', tot_time_astar_h2/(50-Tot_Len_No_Sol_aStar_h2))
#
# print("\n")
# print("###########################_uniform_##############################\n")
#
# print('Total length solution path uniform: ', Tot_Len_Sol_Uniform)
# print('Average length solution path uniform: ',Tot_Len_Sol_Uniform/(50-Tot_Len_No_Sol_Uniform))
#
# print('Total length search path uniform: ', Tot_Len_Sch_Uniform)
# print('Average length search path uniform: ', Tot_Len_Sch_Uniform/(50-Tot_Len_No_Sol_Uniform))
#
# print('Total Number of No solution uniform: ', Tot_Len_No_Sol_Uniform)
# print('Average Number of No solution uniform: ', Tot_Len_No_Sol_Uniform/50)
#
# print('Total cost uniform: ', tot_cost_ucf)
# print('Average cost uniform: ', tot_cost_ucf/(50-Tot_Len_No_Sol_Uniform))
#
# print('Total excution time uniform: ', tot_time_ucf)
# print('Average excution time uniform: ', tot_time_ucf/(50-Tot_Len_No_Sol_Uniform))
#
# print("\n")
# print("##########################_greedy_h1_##############################\n")
#
# print('Total length solution path Greedy_h1: ', Tot_Len_Sol_Greedy_Best_First_h1)
# print('Average length solution path Greedy_h1: ',Tot_Len_Sol_Greedy_Best_First_h1/(50-Tot_Len_No_Sol_Greedy_Best_First_h1))
#
# print('Total length search path Greedy_h1: ', Tot_Len_Sch_Greedy_Best_First_h1)
# print('Average length search path Greedy_h1: ', Tot_Len_Sch_Greedy_Best_First_h1/(50-Tot_Len_No_Sol_Greedy_Best_First_h1))
#
# print('Total Number of No solution Greedy_h1: ', Tot_Len_No_Sol_Greedy_Best_First_h1)
# print('Average Number of No solution Greedy_h1: ', Tot_Len_No_Sol_Greedy_Best_First_h1/50)
#
# print('Total cost Greedy_h1: ', tot_cost_gbfs_h1)
# print('Average cost Greedy_h1: ', tot_cost_gbfs_h1/(50-Tot_Len_No_Sol_Greedy_Best_First_h1))
#
# print('Total excution time Greedy_h1: ', tot_time_gbfs_h1)
# print('Average excution time Greedy_h1: ', tot_time_gbfs_h1/(50-Tot_Len_No_Sol_Greedy_Best_First_h1))
#
# print("\n")
# print("##########################_greedy_h2_##############################\n")
#
# print('Total length solution path Greedy_h2: ', Tot_Len_Sol_Greedy_Best_First_h2)
# print('Average length solution path Greedy_h2: ',Tot_Len_Sol_Greedy_Best_First_h2/(50-Tot_Len_No_Sol_Greedy_Best_First_h2))
#
# print('Total length search path Greedy_h2: ', Tot_Len_Sch_Greedy_Best_First_h2)
# print('Average length search path Greedy_h2: ', Tot_Len_Sch_Greedy_Best_First_h2/(50-Tot_Len_No_Sol_Greedy_Best_First_h2))
#
# print('Total Number of No solution Greedy_h2: ', Tot_Len_No_Sol_Greedy_Best_First_h2)
# print('Average Number of No solution Greedy_h2: ', Tot_Len_No_Sol_Greedy_Best_First_h2/50)
#
#
# print('Total cost Greedy_h2: ', tot_cost_gbfs_h2)
# print('Average cost Greedy_h2: ', tot_cost_gbfs_h2/(50-Tot_Len_No_Sol_Greedy_Best_First_h2))
#
# print('Total excution time Greedy_h2: ', tot_time_gbfs_h2)
# print('Average excution time Greedy_h2: ', tot_time_gbfs_h2/(50-Tot_Len_No_Sol_Greedy_Best_First_h2))
