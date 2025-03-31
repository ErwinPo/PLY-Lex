import ply.lex as lex

tokens = ['INT', 'FLOAT', 'STR']

t_ignore = ' \t'

def t_INT(t):
    r'\d+(_\d+)*'
    t.value = int(t.value.replace('_', ''))
    return t

def t_FLOAT(t):
    r'(\d+(_\d+)*(\.\d*)?|\.\d+(_\d+)*)([eE][+-]?\d+(_\d+)*)?'
    t.value = float(t.value.replace('_', ''))
    return t

def t_STR(t):
    r'"(?:\\.|[^"\\])*"' 
    t.value = t.value 
    return t

def getLexer():
    return lex.lex()