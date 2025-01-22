class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        if isinstance(node, BinOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op == "+":
                return left + right
            elif node.op == "-":
                return left - right
            elif node.op == "*":
                return left * right
            elif node.op == "/":
                return left / right
        elif isinstance(node, NumNode):
            return node.value
        elif isinstance(node, VarNode):
            return self.variables.get(node.name, 0)
        elif isinstance(node, AssignNode):
            self.variables[node.name] = self.visit(node.value)
        elif isinstance(node, PrintNode):
            value = self.visit(node.expr)
            print(value)

