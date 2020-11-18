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
