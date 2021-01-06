import itertools
import time

def imright(h1, h2):
    return h1 - h2 == 1

def nextto(h1, h2):
    return abs(h1 - h2) == 1

def zebra_puzzle():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            if imright(green, ivory)
            for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
            if Englishman is red
            if Norwegian is first
            if nextto(Norwegian, blue)
            for (coffee, tea, milk, oj, WATER) in orderings
            if coffee is green
            if Ukrainian is tea
            if milk is middle
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if Kools is yellow      
            if LuckyStrike is oj
            if Japanese is Parliaments   
            for (dog, snails, fox, horse, ZEBRA) in orderings
            if Spaniard is dog
            if OldGold is snails
            if nextto(Chesterfields, fox)
            if nextto(Kools, horse) 
    )

def timedcall(fn):
    t0 = time.time()
    result = fn
    t1 = time.time()
    return t1 - t0, result

print(timedcall(zebra_puzzle()))

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i += 1 
    
def all_ints():
    yield 0
    for i in ints(1, 10):
        yield +i
        yield -i
        i += 1

L = all_ints()
for i in L:
    print(i)
