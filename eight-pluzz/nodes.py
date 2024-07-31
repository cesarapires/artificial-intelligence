import board
import puzzleState

#Obtain Sub Nodes********************************************************
def subNodes(node, nodesExpanded):

    nodesExpanded = nodesExpanded+1

    nextPaths = []
    nextPaths.append(puzzleState.PuzzleState(board.move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(puzzleState.PuzzleState(board.move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(puzzleState.PuzzleState(board.move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(puzzleState.PuzzleState(board.move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes=[]
    for procPaths in nextPaths:
        if(procPaths.state!=None):
            nodes.append(procPaths)
    return nodes