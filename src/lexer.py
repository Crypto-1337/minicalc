import re

# Definition der verschiedenen Token-Typen
TOKEN_SPECIFICATION = [
    ("NUMBER", r"\d+"),            # Zahlen
    ("ASSIGN", r"="),             # Zuweisung
    ("PLUS", r"\+"),              # Addition
    ("MINUS", r"-"),              # Subtraktion
    ("MULT", r"\*"),              # Multiplikation
    ("DIV", r"/"),                # Division
    ("MOD", r"\%"),               # Modulo
    ("LPAREN", r"\("),            # Linke Klammer
    ("RPAREN", r"\)"),            # Rechte Klammer
    ("SEMICOLON", r";"),          # Semikolon
    ("PRINT", r"print"),          # Keyword: print
    ("VAR", r"[a-zA-Z_][a-zA-Z_0-9]*"), # Variablennamen
    ("SKIP", r"[ \t]+"),          # Leerzeichen (ignorieren)
    ("MISMATCH", r"."),           # Unbekannte Zeichen
]

# Kompilierte Regex für die Token-Erkennung
TOKEN_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPECIFICATION)

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        for match in re.finditer(TOKEN_REGEX, self.code):
            kind = match.lastgroup
            value = match.group(kind)
            if kind == "SKIP":  # Überspringe Leerzeichen
                continue
            elif kind == "MISMATCH":
                raise SyntaxError(f"Ungültiges Zeichen: {value}")
            else:
                self.tokens.append((kind, value))
        return self.tokens

