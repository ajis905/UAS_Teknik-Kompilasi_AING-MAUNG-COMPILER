from am_token import Token
from token_types import TokenType

# =====================
# KEYWORDS
# =====================

KEYWORDS = {
    "lamun": TokenType.LAMUN,
    "ari": TokenType.ARI,
    "sanesna": TokenType.SANESNA,

    "keur": TokenType.KEUR,
    "dina": TokenType.DINA,
    "salila": TokenType.SALILA,
    
    "gawe": TokenType.GAWE,
    "balikeun": TokenType.BALIKKEUN,
    
    "ngomong": TokenType.NGOMONG,
    "nanya": TokenType.NANYA,
    
    "rentang": TokenType.RENTANG,
    "panjang": TokenType.PANJANG,
    
    "enya": TokenType.ENYA,
    "henteu": TokenType.HENTEU,
    
    "catetan": TokenType.CATETAN
}

# =====================
# lEXER
# =====================

class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.current_char = self.source[0] if self.source else None
        self.line = 1
        self.column = 1

    # =========================
    # ADVANCE CHARACTER
    # =========================
    def advance(self):
        self.pos += 1
        self.column += 1

        if self.pos >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.pos]

    # =========================
    # SKIP WHITESPACE
    # =========================
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == "\n":
                self.line += 1
                self.column = 0
            self.advance()

    # =========================
    # WORD (IDENTIFIER / KEYWORD)
    # =========================
    def collect_word(self):
        result = ""

        while self.current_char is not None and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            result += self.current_char
            self.advance()

        if result in KEYWORDS:
            return Token(KEYWORDS[result], result, self.line, self.column)

        return Token(TokenType.IDENTIFIER, result, self.line, self.column)

    # =========================
    # NUMBER
    # =========================
    def collect_number(self):
        result = ""

        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return Token(TokenType.NUMBER, int(result), self.line, self.column)

    # =========================
    # STRING
    # =========================
    def collect_string(self):
        self.advance()  # skip "
        result = ""

        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()

        self.advance()  # skip closing "

        return Token(TokenType.STRING, result, self.line, self.column)

    # =========================
    # MAIN TOKENIZER
    # =========================
    def tokenize(self):
        tokens = []

        while self.current_char is not None:

            # =========================
            # WHITESPACE HANDLING
            # =========================
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # =========================
            # IDENTIFIER / KEYWORD
            # =========================
            if self.current_char.isalpha():
                tokens.append(self.collect_word())
                continue

            # =========================
            # NUMBER
            # =========================
            if self.current_char.isdigit():
                tokens.append(self.collect_number())
                continue

            # =========================
            # STRING
            # =========================
            if self.current_char == '"':
                tokens.append(self.collect_string())
                continue

            # =========================
            # OPERATORS
            # =========================
            if self.current_char == "=":
                self.advance()

                if self.current_char == "=":
                    self.advance()
                    tokens.append(Token(TokenType.EQUAL, "==", self.line, self.column))
                else:
                    tokens.append(Token(TokenType.ASSIGN, "=", self.line, self.column))

                continue

            if self.current_char == "+":
                tokens.append(Token(TokenType.PLUS, "+", self.line, self.column))
                self.advance()
                continue

            if self.current_char == "-":
                tokens.append(Token(TokenType.MINUS, "-", self.line, self.column))
                self.advance()
                continue

            if self.current_char == "*":
                tokens.append(Token(TokenType.MULTIPLY, "*", self.line, self.column))
                self.advance()
                continue

            if self.current_char == "/":
                tokens.append(Token(TokenType.DIVIDE, "/", self.line, self.column))
                self.advance()
                continue

            if self.current_char == "%":
                tokens.append(Token(TokenType.MODULO, "%", self.line, self.column))
                self.advance()
                continue    

            # =========================
            # SYMBOLS
            # =========================
            if self.current_char == "(":
                tokens.append(Token(TokenType.LPAREN, "(", self.line, self.column))
                self.advance()
                continue

            if self.current_char == ")":
                tokens.append(Token(TokenType.RPAREN, ")", self.line, self.column))
                self.advance()
                continue

            if self.current_char == "[":
                tokens.append(
                    Token(
                        TokenType.LBRACKET,
                        "[",
                        self.line,
                        self.column
                    )
                )
                self.advance()
                continue

            if self.current_char == "]":
                tokens.append(
                    Token(
                        TokenType.RBRACKET,
                        "]",
                        self.line,
                        self.column
                    )
                )
                self.advance()
                continue

            if self.current_char == ",":
                tokens.append(
                    Token(
                        TokenType.COMMA,
                        ",",
                        self.line,
                        self.column
                    )
                )
                self.advance()
                continue

            if self.current_char == "{":
                tokens.append(Token(TokenType.LBRACE, "{", self.line, self.column))
                self.advance()
                continue

            if self.current_char == "}":
                tokens.append(Token(TokenType.RBRACE, "}", self.line, self.column))
                self.advance()
                continue

            if self.current_char == ">":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    tokens.append(Token(TokenType.GREATER_EQUAL, ">=", self.line, self.column))
                else:
                    tokens.append(Token(TokenType.GREATER, ">", self.line, self.column))
                continue

            if self.current_char == "<":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    tokens.append(Token(TokenType.LESS_EQUAL, "<=", self.line, self.column))
                else:
                    tokens.append(Token(TokenType.LESS, "<", self.line, self.column))
                continue

            if self.current_char == "!":
                self.advance()

                if self.current_char == "=":
                    self.advance()
                    tokens.append(
                        Token(
                            TokenType.NOT_EQUAL,
                            "!=",
                            self.line,
                            self.column
                        )
                    )
                else:
                    raise Exception("Operator ! teu dikenal")
                continue

            # =========================
            # ERROR HANDLING
            # =========================
            raise Exception(
                f"Kasalahan Lexer di baris {self.line}, kolom {self.column}: '{self.current_char}'"
            )

        tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return tokens