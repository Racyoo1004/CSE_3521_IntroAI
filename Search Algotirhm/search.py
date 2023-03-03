
"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:

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

def depthFirstSearch(problem):
    
    s = util.Stack()
    result = []
    explored = []
  
    start = (problem.getStartState(), [])
    s.push(start)
    
    while not s.isEmpty():
          (state, path) = s.pop()
          
          if problem.isGoalState(state):
                result = path
                break
          
          if state not in explored:
                explored.append(state)
                for curr_state, curr_path, cost in problem.getSuccessors(state):
                      new_path = path + [curr_path]
                      new_state = (curr_state, new_path)
                      s.push(new_state)
                      
    return result

    util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    
    q = util.Queue()
    result = []
    explored = []
    
    start = (problem.getStartState(), [])
    q.push(start)
    
    while not q.isEmpty():
          (state, path) = q.pop()
          
          if problem.isGoalState(state):
                result = path
                break
              
          if state not in explored:
                explored.append(state)
                for curr_state, curr_path, cost in problem.getSuccessors(state):
                      new_path = path + [curr_path]
                      new_state = (curr_state, new_path)
                      q.push(new_state)
                      
    return result
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    
    h = util.PriorityQueue()
    result = []
    explored = []
    
    start = (problem.getStartState(), [], 0)
    h.push(start, start[2])
    
    while not h.isEmpty():
          (state, path, cost) = h.pop()
          
          if problem.isGoalState(state):
                result = path
                break
              
          if state not in explored:
                explored.append(state)
                for curr_state, curr_path, curr_cost in problem.getSuccessors(state):
                      new_cost = cost + curr_cost
                      new_path = path + [curr_path]
                      new_state = (curr_state, new_path, new_cost)
                      h.push(new_state, new_cost)
                      
    return result
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):\
    
    h = util.PriorityQueue()
    result = []
    explored = []
    
    start = (problem.getStartState(), [], 0)
    h.push(start, 0)
    
    while not h.isEmpty():
          state, path, cost = h.pop()
          
          if state not in explored:
                explored = explored + [state]
                
                if problem.isGoalState(state):
                      result = path
                      break
                for curr_state, curr_path, curr_cost in problem.getSuccessors(state):
                      new_cost = cost + curr_cost
                      new_path = path + [curr_path]
                      new_state = (curr_state, new_path, new_cost)
                      h.push(new_state, new_cost + heuristic(curr_state, problem))
                      
    return result
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
