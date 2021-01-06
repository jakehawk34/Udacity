def search(pattern, text):
    """Return true if pattern appears anywhere in text
	   Please fill in the match(          , text) below.
	   For example, match(your_code_here, text)"""
    if pattern.startswith('^'):
        return match(pattern[1:], text) # fill this line
    else:
        return match('.*' + pattern, text) # fill this line

def match(pattern, text): #Returns true if pattern appears at start of text
    '''First condition checks for empty string
    Second checks to see if text is an empty string because $ goes to the end
    Third condition splits pattern into first char, operator, and the rest of the pattern
    '''
    if pattern == '':
        return True
    elif pattern == '$':
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and match(pattern[1:], text[1:]))

    def match1(p, text):
        if not text: return False
        return p == '.' or  p == text[0]
    
    '''
    match(pattern, text) checks if first char p matches 0 times
    match1(p, text) checks if first char p matches the first letter of text
    match_star(p, pattern, text[1:]) checks if it is followed by zero or more occurences of p'''
    def match_star(p, pattern, text):
        return (match(pattern, text) or (match1(p, text) and match_star(p, pattern, text[1:])))