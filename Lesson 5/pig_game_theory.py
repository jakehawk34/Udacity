from functools import update_wrapper

other = {1: 0, 0: 1}

def decorator(d):
    #Make function d a decorator: d wraps a function fn
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    #Decorator that caches the return value for each call to f(args)
    #Whenever it is called again with the same args, we can just look it up
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)
    return _f

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    p, me, you, pending = state
    return (other[p], you, me + pending, 0) #Use other dict to switch player

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    p, me, you, pending = state
    if d == 1:
        state = p, me, you, 1
        return hold(state)
    else:
        return (p, me, you, pending + d)

def Q_pig(state, action, Pwin):
    #The expected value (quality) of choosing action in a state.
    if action == 'hold':
        print(f"expected value of holding from this state: {1 - Pwin(hold(state))}")
        return 1 - Pwin(hold(state))
    elif action == 'roll':
        print(f"expected value of rolling from this state: {(1 - Pwin(roll(state, 1)) + sum(Pwin(roll(state, d)) for d in range(2, 7))) / 6}")
        return (1 - Pwin(roll(state, 1)) 
            + sum(Pwin(roll(state, d)) for d in range(2, 7))) / 6
    raise ValueError


def pig_actions(state):
    #The actions that you can make from a state during the game.
    _, _, _, pending = state
    return ['roll', 'hold'] if pending else ['roll']

goal = 40

@memo
def Pwin(state):
    '''The utility of a state. For this game, utility is the probability that
    an optimal player whose turn it is to move can win from the current state.'''
    #Assumes that the opponent is also playing with the optimal strategy
    (p, me, you, pending) = state
    if me + pending >= goal:
        return 1
    elif you >= goal:
        return 0
    else:
        print(f"probability of winning from this state: {max(Q_pig(state, action, Pwin) for action in pig_actions(state))}")
        return max(Q_pig(state, action, Pwin) for action in pig_actions(state))

def best_action(state, actions, Q, U):
    #Return the oprtimal action for a state, given U.
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)

def max_wins(state):
    return best_action(state, pig_actions, Q_pig, Pwin)

print(max_wins((1, 30, 30, 5)))