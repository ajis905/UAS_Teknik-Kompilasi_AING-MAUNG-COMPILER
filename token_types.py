from enum import Enum, auto


class TokenType(Enum):

    # ==========================
    # Keyword
    # ==========================

    LAMUN = auto()
    ARI = auto()
    SANESNA = auto()

    KEUR = auto()
    DINA = auto()
    SALILA = auto()

    GAWE = auto()
    BALIKKEUN = auto()

    EUREUN = auto()
    TULUY = auto()

    JEUNG = auto()
    ATAWA = auto()
    LAIN = auto()

    ASUPKEUN = auto()

    NGOMONG = auto()
    NANYA = auto()

    RENTANG = auto()
    PANJANG = auto()

    ENYA = auto()
    HENTEU = auto()

    CATETAN = auto()

    # ==========================
    # Identifier & Literal
    # ==========================

    IDENTIFIER = auto()

    NUMBER = auto()

    STRING = auto()

    # ==========================
    # Operator
    # ==========================

    PLUS = auto()

    MINUS = auto()

    MULTIPLY = auto()

    DIVIDE = auto()

    MODULO = auto()

    ASSIGN = auto()

    EQUAL = auto()

    NOT_EQUAL = auto()

    GREATER = auto()

    LESS = auto()

    GREATER_EQUAL = auto()

    LESS_EQUAL = auto()

    # ==========================
    # Delimiter
    # ==========================

    LPAREN = auto()

    RPAREN = auto()

    LBRACE = auto()

    RBRACE = auto()

    LBRACKET = auto()

    RBRACKET = auto()

    COMMA = auto()

    SEMICOLON = auto()

    # ==========================
    # Special
    # ==========================

    EOF = auto()