# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????. 
examples = ['ODD + ODD == EVEN', 'A**2 + B**2 == C**2', 'sum(range(AA)) == BB', 'X / X == X']

import string, re, itertools, time

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            print(f)
    
def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]', formula)))#should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


def timedcall(fn, *args):
    t0 = time.time()
    result = fn(*args)
    t1 = time.time()
    return t1 - t0, result

def test():
    t0 = time.time()
    for example in examples:
        print(example)
        print('{:.4f} sec'.format(timedcall(solve, example)[0]), '\n')
    print('\n', '{:.4f} sec tot'.format(time.time() - t0))

def faster_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda {}: {}'.format(params, body)
    if verbose:
        print(f)
    return eval(f), letters



def compile_word(word):
    if word.isupper():
        #terms = [str(10 ** count) + "*" + letter for count, letter in enumerate(word[::-1])]
        terms = ['{}*{}'.format(10**idx, letter) for idx, letter in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    return word


#test()
print(solve('YOU == ME**2'))
print(faster_solve('YOU == ME**2'))
    