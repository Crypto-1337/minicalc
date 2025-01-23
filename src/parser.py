class ASTNode:
    pass

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumNode(ASTNode):
    def __init__(self, value):
        self.value = value

class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name

class AssignNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class IfNode(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class BlockNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForNode(ASTNode):
    def __init__(self, initialization, condition, increment, body):
        self.initialization = initialization  # Zuweisung (z. B. x = 0)
        self.condition = condition            # Bedingung (z. B. x < 5)
        self.increment = increment            # Inkrement (z. B. x = x + 1)
        self.body = body                      # Block (z. B. { print(x); })

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        nodes = []
        while self.pos < len(self.tokens):
            nodes.append(self.statement())
        return nodes

    def statement(self):
        token_type, token_value = self.tokens[self.pos]
        if token_type == "VAR":
            return self.assignment()
        elif token_type == "PRINT":
            return self.print_statement()
        elif token_type == "IF":
            return self.if_statement()
        elif token_type == "WHILE":
            return self.while_statement()
        elif token_type == "FOR":
            return self.for_statement()
        else:
            raise SyntaxError("Unerwartetes Token: " + token_value)

    def assignment(self):
        var_name = self.tokens[self.pos][1]
        self.pos += 1  # Überspringe VAR
        self.expect("ASSIGN")
        value = self.expression()
        self.expect("SEMICOLON")
        return AssignNode(var_name, value)

    def print_statement(self):
        self.pos += 1  # Überspringe PRINT
        expr = self.expression()
        self.expect("SEMICOLON")
        return PrintNode(expr)

    def while_statement(self):
        self.pos += 1  # Überspringe 'while'
        self.expect("LPAREN")  # Erwarte '('
        condition = self.expression()  # Parse die Bedingung (z. B. x < 5)
        self.expect("RPAREN")  # Erwarte ')'
        body = self.block()  # Parse den Schleifen-Block { ... }
        return WhileNode(condition, body)
    

    def for_statement(self):
        self.pos += 1  # Überspringe 'for'
        self.expect("LPAREN")  # Erwarte '('

        # Parse die Initialisierung (z. B. x = 0)
        initialization = self.assignment()

        # Parse die Bedingung (z. B. x < 5)
        condition = self.expression()
        self.expect("SEMICOLON")  # Erwarte ';'

        # Parse die Inkrementierung (z. B. x = x + 1)
        increment = self.assignment()  # Verwende expression() statt assignment()
        self.expect("RPAREN")  # Erwarte ')'

        # Parse den Schleifenblock
        body = self.block()

        return ForNode(initialization, condition, increment, body)
    def if_statement(self):
        self.pos += 1  # Überspringe 'if'
        self.expect("LPAREN")  # Erwarte '('
        condition = self.expression()  # Bedingung parsen
        self.expect("RPAREN")  # Erwarte ')'
        then_branch = self.block()  # Parsen des 'then'-Blocks
        else_branch = None
        try:
            if self.current_token_type() == "ELSE":
                self.pos += 1  # Überspringe 'else'
                else_branch = self.block()  # Parsen des 'else'-Blocks
        except:
            pass  
        return IfNode(condition, then_branch, else_branch)

    def block(self):
        self.expect("LBRACE")  # Erwarte '{'
        statements = []
        while self.current_token_type() != "RBRACE":
            statements.append(self.statement())  # Parsen von Anweisungen im Block
        self.expect("RBRACE")  # Erwarte '}'
        return BlockNode(statements)

    def expression(self):
        left = self.term()
        while self.current_token_type() in ("PLUS", "MINUS", "DIV", "MULT", "MOD", "GT", "GTEQ", "LT", "LTEQ", "EQ"):
            op = self.current_token_value()
            self.pos += 1
            right = self.term()
            left = BinOpNode(left, op, right)
        return left

    def term(self):
        token_type, token_value = self.tokens[self.pos]
        if token_type == "NUMBER":
            self.pos += 1
            return NumNode(int(token_value))
        elif token_type == "VAR":
            self.pos += 1
            return VarNode(token_value)
        elif token_type == "LPAREN":
            self.pos += 1
            expr = self.expression()
            self.expect("RPAREN")
            return expr
        else:
            raise SyntaxError(f"Unerwartetes Token: {token_value}")

    def expect(self, token_type):
        if self.current_token_type() != token_type:
            raise SyntaxError(f"Erwartet {token_type}, erhalten {self.current_token_type()}")
        self.pos += 1

    def current_token_type(self):
        return self.tokens[self.pos][0]

    def current_token_value(self):
        return self.tokens[self.pos][1]

