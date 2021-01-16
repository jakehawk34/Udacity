from fractions import Fraction
import itertools

sex  = 'BG' #possible genders of a child

day = 'SMTWtFs' #possible days to be born on

def product(*variables):
    #The cartesian product (as a str) of the possibilities for each variable
    return map(''.join, itertools.product(*variables))

two_kids = list(product(sex, sex))

two_kids_bday = list(product(sex, day, sex, day))

one_boy_tuesday = [s for s in two_kids_bday if 'BT' in s]

one_boy = [s for s in two_kids if 'B' in s]

def two_boys(s): return s.count('B') == 2

def condP(predicate, event):
    ''' Conditional probability: P(predicate(s) | s in event).
    The proportion of states in the event for which the predicate is true.'''
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))

print(condP(two_boys, one_boy_tuesday))
