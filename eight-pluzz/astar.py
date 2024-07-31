import time
import nodes
import timeit
import heuristic
import puzzleState
from collections import deque

#Global variables***********************************************
GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None # at finding solution
NodesExpanded = 0 #total nodes visited
MaxSearchDeep = 0 #max deep
MaxFrontier = 0 #max frontier

def astar(startState):
    
    global MaxFrontier, MaxSearchDeep, GoalNode
    
    #transform initial state to calculate Heuritic
    node1 = ""
    for poss in startState:
        node1 = node1 + str(poss)

    #calculate Heuristic and set initial node
    key = heuristic.Heuristic(node1)
    boardVisited= set()
    Queue = []
    Queue.append(puzzleState.PuzzleState(startState, None, None, 0, 0, key)) 
    boardVisited.add(node1)
    
    while Queue:
        Queue.sort(key=lambda o: o.key) 
        node = Queue.pop(0)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = nodes.subNodes(node, NodesExpanded)
        for path in posiblePaths:      
            thisPath = path.map[:]
            if thisPath not in boardVisited:
                key = heuristic.Heuristic(path.map)
                path.key = key + path.depth
                Queue.append(path)               
                boardVisited.add(path.map[:])
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = 1 + MaxSearchDeep

def astarStart(InitialState):
    global GoalNode

    #Start operation
    start = timeit.default_timer()

    astar(InitialState) 

    stop = timeit.default_timer()
    time = stop-start

    #Save total path result
    deep=GoalNode.depth
    moves = []
    while InitialState != GoalNode.state:
        if GoalNode.move == 1:
            path = 'Cima'
        if GoalNode.move == 2:
            path = 'Baixo'
        if GoalNode.move == 3:
            path = 'Esquerda'
        if GoalNode.move == 4:
            path = 'Direita'
        moves.insert(0, path)
        GoalNode = GoalNode.parent

    #'''
    #Print results
    print("################ A* ################")
    print("path: ",moves)
    print("cost: ",len(moves))
    print("nodes expanded: ",str(NodesExpanded))
    print("search_depth: ",str(deep))
    print("MaxSearchDeep: ",str(MaxSearchDeep))
    print("running_time: ",format(time, '.8f'))
    print("####################################")
    #'''

if __name__ == '__main__':
    main()