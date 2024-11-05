import ply.yacc as yacc
from lexer import tokens  # Import tokens from lexer.py
from visualizer import visualize_parse_tree

# Define the grammar rules
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('-', p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_mult(p):
    'term : term MULT factor'
    p[0] = ('*', p[1], p[3])

def p_term_div(p):
    'term : term DIV factor'
    p[0] = ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_parens(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Function to parse an input string
def parse_input(input_string):
    result = parser.parse(input_string)
    return result
    
def evaluate_parse_tree(parse_tree):
    if isinstance(parse_tree, tuple):
        operator, left, right = parse_tree
        left_val = evaluate_parse_tree(left)
        right_val = evaluate_parse_tree(right)
        if operator == '+':
            return left_val + right_val
        elif operator == '-':
            return left_val - right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            return left_val / right_val
    else:
        return parse_tree

if __name__ == "__main__":
    while True:
        try:
            input_string = input('Enter an expression to parse: ')
        except EOFError:
            break
        if not input_string:
            continue

        result = parse_input(input_string)
        if result is not None:
            print(f"Parsed result: {result}")
            visualize_parse_tree(result)
            evaluated_result = evaluate_parse_tree(result)
            print(f"Evaluated result: {evaluated_result}")
        else:
            print("Invalid expression")
