import ply.lex as lex

tokens = ['INT', 'ID']

t_INT = r'[0-9]+'
t_ID = r'[a-z][a-z0-9]*'

t_ignore = ' \n*(=;)'

scanner = lex.lex()

scanner.input("area = (pi * radius ** 2);")

while True:
    token = scanner.token()
    if not token:
        break
    print(token)