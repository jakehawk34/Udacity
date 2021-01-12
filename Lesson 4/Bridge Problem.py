import doctest

def bridge_problem(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set() #set of states we have visited
    #State is (people-here, people-there, time elapsed) tuple
    frontier = [ [(here, frozenset(), 0)] ] #ordered list of paths
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0) #Pop the first element from frontier
        here1, there1, t1 = state1 = path[-1] #Test after popping off
        if not here1:
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
    return []

def elapsed_time(path):
    return path[-1][2]

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""

    '''If the light is here, the person or people will move to there
    Return a dictionary that contains:
    1. A key of a tuple with:
        -here subtracted by the people and light after the action
        -The union of there and who moved from here after the action
        -The sum of the elapsed time plus the people's max travel time after the move
    2. A value of a tuple with:
        -The first person (person1)
        -The second person (person2); can be same as person1 if only one person moved
        -The direction of the move for the action (-> for here to there)
    '''
    here, there, t = state

    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']), 
        there | frozenset([a, b, 'light']), 
        t + max(a, b)), (a, b, '->')) 
        for a in here if a != 'light' 
        for b in here if b != 'light')
    #If the light is there, the person or people will move to here
    else:
        return dict(((here | frozenset([a, b, 'light']),
        there - frozenset([a, b, 'light']),
        t + max(a, b)), (a, b, '<-'))
        for a in there if a != 'light'
        for b in there if b != 'light')

#Return a list of the states for a path
def path_states(path):
    return path[::2]

#Return a list of the actions for a path
def path_actions(path):
    return path[1::2]

print(bridge_problem([1, 2, 3]))

#print(f'''The most efficient solution took 
#{len(path_actions(bridge_problem((1,2,5,10))))} actions 
#and a total of {bridge_problem((1, 2, 5, 10))[-1][-1]} seconds''')

class TestBridge: """
>>> elapsed_time(bridge_problem([1,2,5,10]))
17

## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> [elapsed_time(bridge_problem([1,2,4,8,16][:N])) for N in range(1, 6)]
[1, 2, 7, 15, 28]

>>> [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(1, 8)]
[1, 1, 2, 6, 12, 19, 30]

>>> elapsed_time(bridge_problem([1, 2, 3]))
6

>>> [elapsed_time(bridge_problem([1, 2, 3][:N])) for N in range(1, 4)]
[1, 2, 6]
"""

print(doctest.testmod())