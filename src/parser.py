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

    def expression(self):
        left = self.term()
        while self.current_token_type() in ("PLUS", "MINUS"):
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

