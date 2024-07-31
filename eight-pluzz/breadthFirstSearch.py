import time
import nodes
import timeit
import argparse
import heuristic
import puzzleState
from collections import deque

#Global variables***********************************************
GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None # at finding solution
NodesExpanded = 0 #total nodes visited
MaxSearchDeep = 0 #max deep
MaxFrontier = 0 #max frontier

def bfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited= set()
    Queue = deque([puzzleState.PuzzleState(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = nodes.subNodes(node, NodesExpanded)
        for path in posiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize        
  
#MAIN**************************************************************
def bfsStart(InitialState):
    global GoalNode

    #Start operation
    start = timeit.default_timer()

    bfs(InitialState)

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
    print("################ Busca em Amplitude ################")
    print("path: ",moves)
    print("cost: ",len(moves))
    print("nodes expanded: ",str(NodesExpanded))
    print("search_depth: ",str(deep))
    print("MaxSearchDeep: ",str(MaxSearchDeep))
    print("running_time: ",format(time, '.8f'))
    print("####################################################")
    #'''

if __name__ == '__main__':
    main()