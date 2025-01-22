import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    with open(sys.argv[1]) as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    for node in ast:
        interpreter.visit(node)

if __name__ == "__main__":
    main()

