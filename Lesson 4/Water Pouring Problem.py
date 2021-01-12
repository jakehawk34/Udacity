def pour_problem(X, Y, goal, start=(0,0)):
    '''X and Y are the capacity of the glasses; (x, y) is the current fill levels
    and represents a state. The goal is a level that can be in either glass. 
    Start at the start state and follow successors until we reach the goal.
    Keep track of the frontier and previously explored paths;
    fail when the frontier is empty.
    '''
    if goal in start:
        return [start]
    explored = set()
    frontier = [ [start] ]
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1]
        for (state, action) in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

'''Return a dictionary of (state: action) pairs that can be reached from
the current (x, y) state and how.'''
def successors(x, y, X, Y):
    #x and y are current glass levels; X and Y are glass sizes
    assert x <= X and y <= Y 
    return {(X, y): 'fill X',
            (x, Y): 'fill Y',
            (0, y): 'empty X',
            (x, 0): 'empty Y',
            (0, x+y) if x+y <= Y else (x - (Y - y), y + (Y - y)): 'X -> Y',
            (y+x, 0) if y+x <= X else (x + (X - x), y - (X - x)): 'Y -> X'}

print(pour_problem(4, 9, 6))
