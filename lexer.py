import ply.lex as lex

# List of token names
# The priority applies in the same order as the tokens are specified -> higher index implies higher priority
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'MULT', 'DIV',
    'LPAREN', 'RPAREN',
)

# Regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Token for number
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters 
t_ignore = ' \t'

# Disallow illegal characters
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
