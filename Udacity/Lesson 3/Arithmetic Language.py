import re
from functools import update_wrapper



def grammar(description, whitespace=r'\s*'):
    #Convert a description to a grammar
    G = {' ': whitespace}
    description = description.replace('\t', ' ') #Replaces tabs with space
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G

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

def split(text, sep=None, maxsplit=-1):
    #Similar to str.split applied to text,
    #but strips whitespace away from each piece
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]

def parse(start_symbol, text, grammar):
    '''Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed
    the whole string. Failure iff remainder is None. This is a deterministic
    Parse Expression Grammar (PEG) parser, so rule order (left-to-right) matters.
    Do 'E' => T op E | T' putting the longest parse first; dont' do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T' '''

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text, = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    @memo
    def parse_atom(atom, text):
        if atom in grammar: #Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom] + tree, rem
            return Fail
        else: #Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            if (not m):
                return Fail 
            else: 
                return (m.group(), text[m.end():])
    
    #Body of parse:
    return parse_atom(start_symbol, text)

Fail = (None, None)

G = grammar(r'''
Exp => Term [+-] Exp) | Term
Term => Factor [*/] Term | Factor
Factor => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps => Exp [,] Exps | Exp
Var => [a-zA-Z_]\w*
Num => [-+]?[0-9]+([.][0-9]*)?
''')

parse('Exp', '3*x + b', G)