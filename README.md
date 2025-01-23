MiniCalc Interpreter
====================

MiniCalc is a simple, minimalistic programming language with an interpreter written in python. It was created as a learning project to explore the fundamentals of compiler and interpreter design, including lexing, parsing, abstract syntax tree (AST) generation, and execution.

Features
--------

*   x = 5;y = x + 3;
    
*   result = (5 + 3) \* 2;
    
*   if (x > 10) {print(x);} else {print(0);}
    
*   x = 0;while (x < 5) { print(x); x = x + 1;}
    

Syntax Rules
------------

1.  **Statements**: Every statement ends with a semicolon (;).
    
2.  **Blocks**: Code blocks are enclosed in curly braces {}.
    
3.  **Expressions**: Arithmetic operations (+, -, \*, /) and comparisons (<, >, ==) are supported.
    
4.  **Whitespace**: Whitespace is ignored except when it separates tokens.
    
5.  **Reserved Keywords**: if, else, while, and print are reserved.
    

Installation and Usage
----------------------

1.  git clone cd MiniCalc
    
2.  python3 src/main.py examples/example1.mc
    
3.  x = 10;y = x + 5;if (y > 10) { print(y);}
    

How It Works
------------

1.  **Lexical Analysis**: The lexer.py converts the source code into tokens:
    
    *   x = 10;Becomes:\[('VAR', 'x'), ('ASSIGN', '='), ('NUMBER', '10'), ('SEMICOLON', ';')\]
        
2.  **Parsing**: The parser.py takes the tokens and builds an Abstract Syntax Tree (AST):
    
    *   x = 10;Becomes:AssignNode( name="x", value=NumNode(10))
        
3.  **Execution**: The interpreter.py walks the AST and evaluates the nodes:
    
    *   x = 10;print(x);Outputs:10
        
Contribution
------------

Contributions are welcome! If you encounter issues or have ideas for improvements, feel free to submit a pull request or open an issue.
