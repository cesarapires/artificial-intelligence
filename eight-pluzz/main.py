import astar
import argparse
import breadthFirstSearch

#To test call main.py 1,4,5,7,8,2,3,6,0
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('initialBoard')
    args = parser.parse_args()
    data = args.initialBoard.split(",")

    #Build initial board state
    InitialState = []
    InitialState.append(int(data[0]))
    InitialState.append(int(data[1]))
    InitialState.append(int(data[2]))
    InitialState.append(int(data[3]))
    InitialState.append(int(data[4]))
    InitialState.append(int(data[5]))
    InitialState.append(int(data[6]))
    InitialState.append(int(data[7]))
    InitialState.append(int(data[8]))

    astar.astarStart(InitialState)

    breadthFirstSearch.bfsStart(InitialState)

if __name__ == '__main__':
    main()