import doctest

def lowest_cost_search(start, successors, is_goal, action_cost):
    """Return the lowest cost path, starting from start state,
    and considering successors(state) => {state:action,...},
    that ends in a state for which is_goal(state) is true,
    where the cost of a path is the sum of action costs,
    which are given by action_cost(action)."""
    Fail = []
    
    explored = set() # set of states we have visited
    # State will be a (peoplelight_here, peoplelight_there) tuple
    # E.g. ({1, 2, 5, 10, 'light'}, {})
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        state1 = final_state(path)
        if is_goal(state1):  
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in successors(state1).items():
            if state not in explored:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail

def bridge_problem3(here):
    """Find the fastest (least elapsed time) path to 
    the goal in the bridge problem."""
    start = (frozenset(here) | frozenset(['light']), frozenset())
    def all_over(state):
        here, there = state
        return not here or here == set('light')

    return lowest_cost_search(start, bsuccessors2, all_over, bcost)

def bridge_problem2(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set() #set of states we have visited
    #State is (peoplelight-here, peoplelight-there) tuple
    frontier = [ [(here, frozenset())] ] #ordered list of paths
    while frontier:
        path = frontier.pop(0) #Pop the first element from frontier
        here1, there1 = state1 = final_state(path) #Test after popping off
        if not here1 or (len(here1)==1 and 'light' in here1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in bsuccessors2(state1).items():
            if state not in explored:
                total_cost = pcost + bcost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return []

def final_state(path): 
    return path[-1]

def add_to_frontier(frontier, path):
    'Add path to frontier, replacing costlier path if there is one.'
    #Find if there is an old path to the final state of this path
    old  = None
    for i, p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return #Old past was better, so do nothing
    elif old is not None:
        del frontier[old] #Old path was worse; delete it
    # Now add the new path and re-sort the frontier
    frontier.append(path)

def elapsed_time(path):
    return path[-1][2]

def bsuccessors2(state):

    here, there = state

    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']), 
            there | frozenset([a, b, 'light'])), 
            (a, b, '->')) 
            for a in here if a != 'light' 
            for b in here if b != 'light')
    #If the light is there, the person or people will move to here
    else:
        return dict(((here | frozenset([a, b, 'light']),
            there - frozenset([a, b, 'light'])),
            (a, b, '<-'))
            for a in there if a != 'light'
            for b in there if b != 'light')

#Return a list of the states for a path
def path_states(path):
    return path[::2]

#Return a list of the actions for a path
def path_actions(path):
    return path[1::2]

#The total cost of a path, which is stored in a tuple with an action
#path = [state, (action, total_cost), action, ...]
def path_cost(path):
    if len(path) < 3:
        return 0
    else:
        actions, total_cost = path[-2]
        return total_cost

#The total cost of an action in the bridge problem
def bcost(action):
    a, b, arrow = action
    return max(a, b)

test = bridge_problem3([1, 2, 5, 10])

print(path_actions(test))
print(path_cost(test))