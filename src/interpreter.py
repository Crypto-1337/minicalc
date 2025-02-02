# Importiere die AST-Klassen
from parser import *

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
            elif node.op == "<=":
                return left <= right
            elif node.op == ">":
                return left > right
            elif node.op == ">=":
                return left >= right
            elif node.op == "==":
                return left == right
        elif isinstance(node, NumNode):  # Zahlen
            return node.value
        elif isinstance(node, StringNode):
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
        elif isinstance(node, WhileNode):
            while self.visit(node.condition):
                self.visit(node.body);
        elif isinstance(node, ForNode):
            self.visit(node.initialization)
            while self.visit(node.condition):  # Bedingung prüfen
                self.visit(node.body)         # Block ausführen
                self.visit(node.increment)    # Inkrement ausführen
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
