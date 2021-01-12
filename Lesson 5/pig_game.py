'''
Win: Utility of 1 
Lose: Utility of 0
I choose the best option for me
Opponent chooses the worst option for me
Dice averages out (random)
Utility(state) -> number
Quality(state, action) -> number. For example, Q(state, roll) or Q(s, hold)
Game Theory - decision under uncertainty against an opponent
Decision theory - decision under uncertainty
'''

from collections import namedtuple
import random

State = namedtuple('State', 'p, me, you, pending')
other = {1:0, 0:1}
goal = 50

def play_pig(A, B):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    
    strategies = [A, B]
    state = (0, 0, 0, 0)
    while True:
        (p, me, you, pending) = state
        if me >= goal:
            return strategies[p]
        elif you >= goal:
            return strategies[other[p]]
        elif strategies[p](state) == 'hold':
            state = hold(state)
        else:
            d = random.randint(1, 6)
            state = roll((state), d)
    

def always_roll(state):
    return 'roll'

def always_hold(state):
    return 'hold'

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

def hold_at(x):
    """Return a strategy that holds if and only if 
    pending >= x or player reaches goal."""
    def strategy(state):
        (p, me, you, pending) = state
        if pending >= x or me + pending == goal:
            return 'hold'
        else: return 'roll'
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy

print(play_pig(always_roll, always_hold).__name__)

tally = [0, 0]
for i in range(10000):
    x = play_pig(hold_at(20), hold_at(25))
    if x.__name__ == 'hold_at(20)':
        tally[0] += 1
    else:
        tally[1] += 1

percent_A = tally[0] / sum(tally) * 100
percent_B = tally[1] / sum(tally) * 100
#print(percent_A, percent_B)


