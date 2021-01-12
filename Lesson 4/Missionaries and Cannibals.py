import numpy as np

def shortest_path_search(start, successors, is_goal):
    if is_goal(start):
        return [start]
    explored = set() #set of states we have visited
    frontier = [ [start] ] #ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

def mc_problem2(start=(3, 3, 1, 0, 0, 0), goal=None):
    # your code here if necessary
    if goal == None:
        def goal_fn(state): return state[:3] == (0, 0, 0)
    else:
        def goal_fn(state): return state == goal
    return shortest_path_search(start, csuccessors, goal_fn)

def mc_problem(start=(3, 3, 1, 0, 0, 0), goal=None):
    '''Solve the missionaries and cannibals problem.
    State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start (1) and other (2) sides.
    Find a path that goes from the initial state to the goal state (which, by default,
    is the state with no people and no boats on the start side)'''
    if goal is None:
        goal = (0, 0, 0) + start[:3]
    if start == goal:
        return [start]
    explored = set() #set of states we have visited
    frontier = [ [start] ] #ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in csuccessors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

#Use numpy to subtract each delta in the deltas dict when the boat goes from start side to the other side
#Add each delta when the boat goes from the other side back to the start
#B1 will always be equal to -B2
def csuccessors(state):
    M1, C1, B1, M2, C2, B2 = state
    #Check for state with at least one missionary and a great amount of cannibals
    if C1 > M1 > 0 or C2 > M2 > 0 or M1 < 0 or M2 < 0:
        return {}
    items = []
    if B1 > 0:
        items += [(tuple(np.subtract(state, delta)), a + '->') for delta, a in deltas.items()]
    if B2 > 0:
        items += [(tuple(np.add(state, delta)), '<-' + a) for delta, a in deltas.items()]
    return dict(items)

#Dictionary to store the changes in values for M, C, and B
deltas = {(1, 0, 1, -1, 0, -1): 'M', 
          (0, 1, 1, 0, -1, -1): 'C',
          (1, 1, 1, -1, -1, -1): 'MC',
          (2, 0, 1, -2, 0, -1): 'MM',
         (0, 2, 1, 0, -2, -1): 'CC'}

print(mc_problem2())
