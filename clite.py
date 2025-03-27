import ply.lex as lex

tokens = ['FLOAT', 'INT']

t_ignore = ' \t'

# Define el reconocimiento de números flotantes básicos
def t_FLOAT(t):
    r'(\d+\.\d*|\.\d+|\d+\.)'
    t.value = float(t.value)
    return t

# Define el reconocimiento de números enteros
def t_INT(t):
    r'\d+(_\d+)*'
    t.value = int(t.value.replace('_', ''))
    return t

def getLexer():
    return lex.lex()
