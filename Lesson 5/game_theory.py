
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
import math

million = 1000000

def Q(state, action, U):
    "The expected value of taking action in state, according the utility U"
    if action == "hold":
        print(round(U(state + 1*million)))
        return U(state + 1*million)
    if action == "gamble":
        print(round(U(state + 3*million) * 0.5 + U(state) * 0.5))
        return U(state + 3*million) * 0.5 + U(state) * 0.5

def actions(state): return ['hold', 'gamble']

def identity(x): return x

U = math.log10

def best_action(state, actions, Q, U):
    #Return the oprtimal action for a state, given U.
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)



print(best_action(1.5*million, actions, Q, U))

gamble = (c for c in range(1, 10) 
         if Q(c*million, 'gamble', U) == Q(c*million, 'hold', U))

print(next(gamble))




