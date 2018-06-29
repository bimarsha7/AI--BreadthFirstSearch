from collections import deque
import time

########       c        ########
#      b   ##  a   ##  d 
#    e  f ## g  h ## i j
#       k
#we have assumed that c is the rootnode whille k is the goal node
#you may change the adjacency_list yourself to add aor delete any nodes as you wish
#you may select any rootNode and any goalState
class Node:
    def __init__(self,rootNode, goalState):
        self.rootNode = rootNode  #the node you are starting your search
        self.goalState = goalState

    def bfs(self,adjacency_list):
        frontier = deque([self.rootNode])
        explored = set()
     
        while len(frontier) != 0:
            state = frontier.popleft() #now the node is remode from the queue
            print(state)  
            time.sleep(0.5)
            explored.add(state) #thus is now added to explored set
            if state == self.goalState:
                return True
            if state in adjacency_list: #check if the key() of adjacency_list
                for neighbour in adjacency_list[state]:
                    if neighbour not in frontier or explored:
                        frontier.append(neighbour)             
        return None

def main():
    #initialize class Node with initial-state and goal-state of your search agent
    nd = Node('c', 'k')

    #create graph of adjacency list for searching
    adjacency_list = { 
    'c':['b', 'a', 'd'],
    'b':['e', 'f'],
    'a':['g', 'h'],
    'd':['i', 'j'],
    'f':['k']
    }  
    print(nd.bfs(adjacency_list))
    

if __name__ == "__main__":
    main()