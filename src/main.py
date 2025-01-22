from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    code = """
    x = 10;
    y = x + 5;
    print(y);
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    for node in ast:
        interpreter.visit(node)

if __name__ == "__main__":
    main()

