# Write a function, readwordlist, that takes a filename as input and returns
# a set of all the words and a set of all the prefixes in that file, in 
# uppercase. For testing, you can assume that you have access to a file 
# called 'words4k.txt'

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename) # opens file
    text = file.read()    # gets file into string
    wordset = set(text.upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset


def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

    
WORDS, PREFIXES = readwordlist('words4k.txt')

#Nested function version
def find_words(letters):
    results = set()

    def extend_prefix(w, letters):
        if w in WORDS: results.add(w)
        if w not in PREFIXES: return
        #Extend the prefix by one letter, L. 
        #removed(letters, L) are the letters we have remaining to add to the word
        for L in letters:
            extend_prefix(w + L, removed(letters, L))

    extend_prefix('', letters)
    return results

#Flat version
def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre + L, letters.replace(L, '', 1), results)
    return results

#Alternate flat version with find_words as a recursive function
def find_words(letters, pre='', results=None):
    if results is None: results = set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words(letters.replace(L, '', 1), pre + L, results)
    return results
