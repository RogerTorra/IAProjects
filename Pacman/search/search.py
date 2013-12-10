# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import sys
import node
import time

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def breadthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    #fringe = [node.Node(problem.getStartState(),None,None,0)] #iniciamos la frontera con el estado inicial
    start = time.clock()
    fringe = util.Queue() #usamos la clase cola en util
    fringe.push(node.Node(problem.getStartState(),None,None,0,0))
    expanded = {}
    print "Start:", problem.getStartState()

    while True:
        if fringe.isEmpty():
            sys.exit('No solution')
        n = fringe.pop()
        expanded[n.state] = ['E',n]
        if problem.isGoalState(n.state):
            print "TIME:", (time.clock() - start)
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            if state not in expanded:
                ns = node.Node(state, n,action, n.pathcost + cost, n.depth + 1)
                fringe.push(ns)
                expanded[state] = ['F',ns]

def breadthFirstSearchTree(problem):
    start = time.clock()
    fringe = util.Queue() #usamos la clase cola en util
    fringe.push(node.Node(problem.getStartState(),None,None,0,0))
    print "Start:", problem.getStartState()
    while True:
        if fringe.isEmpty():
            sys.exit('No solution')
        n = fringe.pop()
        if problem.isGoalState(n.state):
            print "TIME:", (time.clock() - start)
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            ns = node.Node(state, n,action, n.pathcost + cost, n.depth + 1)
            fringe.push(ns)
    util.raiseNotDefined()


def depthFirstSearch(problem):

   
    "*** YOUR CODE HERE ***"
    start = time.clock()
    fringe = util.Stack() #usamos la clase pila en util
    fringe.push(node.Node(problem.getStartState(),None,None,0,0))
    expanded = {}
    print "Start:", problem.getStartState()

    while True:
        if fringe.isEmpty():
            sys.exit('No solution')

        n = fringe.pop()
        expanded[n.state] = ['E',n]
        if problem.isGoalState(n.state):
            #print n.path
            #sys.exit('Solution')
            print "TIME:", (time.clock() - start)
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            #print action , " -> " , state
            if state not in expanded:
                ns = node.Node(state, n,action, n.pathcost + cost, n.depth + 1)
                fringe.push(ns)
                expanded[state] = ['F',ns]

    util.raiseNotDefined()


def depthFirstSearchTree(problem):

   
    "*** YOUR CODE HERE ***"
    start = time.clock()
    fringe = util.Stack() #usamos la clase pila en util
    fringe.push(node.Node(problem.getStartState(),None,None,0,0))
    print "Start:", problem.getStartState()
    while True:
        if fringe.isEmpty():
            sys.exit('No solution')
        n = fringe.pop()
        if problem.isGoalState(n.state):
            #print n.path
            #sys.exit('Solution')
            print "TIME:", (time.clock() - start)
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            #print action , " -> " , state
            ns = node.Node(state, n,action, n.pathcost + cost, n.depth + 1)
            fringe.push(ns)

    util.raiseNotDefined()
"""
def uniformCostSearch2(problem):

    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue() #usamos la clase cola con prioridad en util
    fringe.push(node.Node(problem.getStartState(),None,None,0),0) #con coste 0
    expanded = {}
    print "Start:", problem.getStartState()

    while True:
        if fringe.isEmpty():
            sys.exit('No solution')

        n = fringe.pop()
        expanded[n.state] = ['E',n]
        if problem.isGoalState(n.state):
            #print n.path
            #sys.exit('Solution')
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            #print action , " -> " , state
            if state not in expanded:
                ns = node.Node(state, n,action, n.pathcost + cost)
                if action == "South":
                    fringe.push(ns, n.pathcost+10)
                if action == "Right":
                    fringe.push(ns, n.pathcost+10)
                else:
                    fringe.push(ns, n.pathcost)
                    expanded[state] = ['F',ns]
           # else if ns with n.pathcost not in fringe

    util.raiseNotDefined()
"""
def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    start = time.clock()
    fringe = util.PriorityQueue() #usamos la clase cola con prioridad en util
    fringe.push(node.Node(problem.getStartState(),None,None,0,0),0) #con coste 0
    expanded = {}
    print "Start:", problem.getStartState()

    while True:
        if fringe.isEmpty():
            sys.exit('No solution')
        n = fringe.pop()
        expanded[n.state] = ['E',n]
        if problem.isGoalState(n.state):
            print "TIME:", (time.clock() - start)
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            if state not in expanded:
                ns = node.Node(state, n,action, n.pathcost + cost , n.depth +1)
                fringe.push(ns, n.pathcost)
                expanded[state] = ['F',ns]

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

def euclidean( xy1, xy2 ):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5

def aStarSearch(problem, heuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    start = time.clock()
    fringe = util.PriorityQueue() #usamos la clase cola con prioridad en util
    print "Start: ", problem.getStartState()
    print "Finish: ", problem.goal
    h = heuristic(problem.getStartState(), problem.goal)
    fringe.push(node.Node(problem.getStartState(),None,None,0,0),h) #con coste h(n)
    expanded = {}  
    while True:
        if fringe.isEmpty():
            sys.exit('No solution')
        n = fringe.pop()
        expanded[n.state] = ['E',n]
        if problem.isGoalState(n.state):
            print "TIME:", (time.clock() - start)
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            if state not in expanded:
                h = heuristic(state, problem.goal)
                ns = node.Node(state, n,action, n.pathcost + h , n.depth +1)
                fringe.push(ns, n.pathcost)
                expanded[state] = ['F',ns]
    
    

    util.raiseNotDefined()

def limitedDS(problem,k):
    fringe = util.Stack() #usamos la clase pila en util
    fringe.push(node.Node(problem.getStartState(),None,None,0,0))
    expanded = {}
    cut = False
    print "Start:", problem.getStartState()
   
    print "K :",k
    while True:
        if fringe.isEmpty():
            if cut: return 'cutoff' 
            else: return 'No solution'
        n = fringe.pop()
        expanded[n.state] = ['E',n]
        if n.depth == k:
            cut = True
        if problem.isGoalState(n.state):
            
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            if state not in expanded:
                ns = node.Node(state, n,action, n.pathcost + cost, n.depth+1)
                fringe.push(ns)
                expanded[state] = ['F',ns]

    util.raiseNotDefined()

def iterativeDS(problem):
    start = time.clock()
    k = problem.getStartState()[0] * problem.getStartState()[1]
    for i in range(0,k):
        result = limitedDS(problem,k)
        if result is not 'cutoff':
            print "TIME:", (time.clock() - start)
            return result

def greedyBFS(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    start = time.clock()
    fringe = util.PriorityQueue() #usamos la clase cola con prioridad en util
    print "Start:", problem.getStartState()
    print "Finish:", problem.goal
    h = util.manhattanDistance(problem.getStartState(), problem.goal)
    fringe.push(node.Node(problem.getStartState(),None,None,0,0),h) #con coste h(n)
    expanded = {}  
    while True:
        if fringe.isEmpty():
            sys.exit('No solution')
        n = fringe.pop()
        expanded[n.state] = ['E',n]
        if problem.isGoalState(n.state):
            print "TIME:", (time.clock() - start)
            return  n.path()
        for state,action,cost in problem.getSuccessors(n.state):
            if state not in expanded:
                h = util.manhattanDistance(state, problem.goal)
                ns = node.Node(state, n,action, n.pathcost + h + cost, n.depth +1)
                fringe.push(ns, n.pathcost)
                expanded[state] = ['F',ns]

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
bfst = breadthFirstSearchTree
dfs = depthFirstSearch
dfst = depthFirstSearchTree
astar = aStarSearch
ucs = uniformCostSearch
lds = limitedDS
ids = iterativeDS
gbfs = greedyBFS

if __name__ == "__main__": #test unitario

    greedyBFS (mediumMaze)