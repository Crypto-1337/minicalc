# Importiere die AST-Klassen
from parser import BinOpNode, NumNode, AssignNode, VarNode, PrintNode, IfNode, BlockNode

class Interpreter:
    def __init__(self):
        self.variables = {}  # Variablenspeicher

    def visit(self, node):
        if isinstance(node, BinOpNode):  # Mathematische Operationen
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
            elif node.op == "%":
                return left % right
            elif node.op == "<":
                return left < right
            elif node.op == ">":
                return left > right
            elif node.op == "==":
                return left == right
        elif isinstance(node, NumNode):  # Zahlen
            return node.value
        elif isinstance(node, VarNode):  # Variablen
            if node.name not in self.variables:
                raise NameError(f"Variable '{node.name}' ist nicht definiert.")
            return self.variables[node.name]
        elif isinstance(node, AssignNode):  # Zuweisungen
            self.variables[node.name] = self.visit(node.value)
        elif isinstance(node, PrintNode):  # Druckbefehl
            value = self.visit(node.expr)
            print(value)
        elif isinstance(node, IfNode):  #Bedingung
            condition_value = self.visit(node.condition)
            if condition_value:
                self.visit(node.then_branch)
            elif node.else_branch:
                self.visit(node.else_branch)
        elif isinstance(node, BlockNode):
            for statement in node.statements:
                self.visit(statement)
        else:
            raise TypeError(f"Unbekannter Knotentyp: {type(node)}")
