from cProfile import label
from token_types import TokenType
from parse_tree import ParseTreeNode
from ast_nodes import (
    AssignNode,
    CallNode,
    IfNode,
    AriNode,
    ElseNode,
    ConditionNode,
    BinaryOpNode,
    WhileNode,
    ForNode,
    ArrayNode,
    IndexNode,
    FunctionNode,
    ReturnNode, 
    StringNode,
    IndexAssignNode,
)

# =====================
# PARSER
# =====================

class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.pos = 0
        self.current = self.tokens[self.pos]
        self.parse_tree_root = ParseTreeNode("Program")

        self.current_tree_parent = self.parse_tree_root

    def add_parse_tree(self, parent, label, value=None):
        """
        Helper untuk membuat Parse Tree lebih rapi.
        """
        node = ParseTreeNode(label)

        if value is not None:
            node.value = str(value)

        parent.add_child(node)

        return node


    # =========================
    # ADVANCE & EXPECT
    # =========================

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]

    def expect(self, token_type):
        if self.current.type == token_type:
            self.advance()
        else:
            raise Exception(f"Syntax Error: expected {token_type}, got {self.current.type}")

    # =========================
    # PARSE
    # =========================

    def parse(self):
        statements = []
        while self.current.type != TokenType.EOF:
            statements.append(self.statement())
        return statements

    # =========================
    # STATEMENT
    # =========================

    def statement(self):

        # IF
        if self.current.type == TokenType.LAMUN:
            return self.if_statement()
        
        if self.current.type == TokenType.SALILA:
            return self.while_statement()
        
        elif self.current.type == TokenType.KEUR:
            return self.for_statement()

        # ARI
        if self.current.type == TokenType.ARI:
            return self.ari_statement()

        # ELSE
        if self.current.type == TokenType.SANESNA:
            return self.else_statement()

        # FUNCTION CALL
        if self.current.type == TokenType.NGOMONG:
            return self.function_call()
        
        # FUNCTION DEFINITION
        if self.current.type == TokenType.GAWE:
            return self.function_definition()
        
        # RETURN
        elif self.current.type == TokenType.BALIKKEUN:
            return self.return_statement()

        # IDENTIFIER
        if self.current.type == TokenType.IDENTIFIER:

            next_token = (
                self.tokens[self.pos + 1]
                if self.pos + 1 < len(self.tokens)
                else None
            )

            # angka[1] = ...
            if next_token and next_token.type == TokenType.LBRACKET:

                i = self.pos + 2
                bracket = 1

                while i < len(self.tokens):

                    if self.tokens[i].type == TokenType.LBRACKET:
                        bracket += 1

                    elif self.tokens[i].type == TokenType.RBRACKET:
                        bracket -= 1

                        if bracket == 0:
                            break

                    i += 1

                # angka[1] = ...
                if (
                    i + 1 < len(self.tokens)
                    and self.tokens[i + 1].type == TokenType.ASSIGN
                ):
                    return self.index_assignment()

                # angka[1]
                return self.expression()

            # hasil = ...
            if next_token and next_token.type == TokenType.ASSIGN:
                return self.assignment()

            # tambah(...)
            if next_token and next_token.type == TokenType.LPAREN:
                return self.expression()

            raise Exception("Syntax Error: statement teu dikenal.")

    # =========================
    # ASSIGNMENT 
    # =========================

    def assignment(self):
        name = self.current.value

        self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.ASSIGN)

        value = self.expression()

        assign_node = self.add_parse_tree(
            self.current_tree_parent,
            "Assignment"
        )

        self.add_parse_tree(
            assign_node,
            "IDENTIFIER",
            name
        )

        self.add_parse_tree(
            assign_node,
            "VALUE",
            value
        )

        value_type = type(value)

        return AssignNode(
            name,
            value,
            value_type
        )

    # =========================
    # ARRAY INDEX ASSIGNMENT
    # =========================

    def index_assignment(self):

        array = self.current.value
        self.expect(TokenType.IDENTIFIER)

        self.expect(TokenType.LBRACKET)

        index = self.expression()

        self.expect(TokenType.RBRACKET)

        self.expect(TokenType.ASSIGN)

        value = self.expression()

        node = self.add_parse_tree(
            self.current_tree_parent,
            "Array Assignment"
        )

        self.add_parse_tree(
            node,
            "ARRAY",
            array
        )

        self.add_parse_tree(
            node,
            "INDEX",
            index
        )

        self.add_parse_tree(
            node,
            "VALUE",
            value
        )

        return IndexAssignNode(
            array,
            index,
            value
        )

    # =========================
    # IF
    # =========================

    def if_statement(self):
        self.expect(TokenType.LAMUN)

        condition = self.condition()

        body = []

        # Support either a braced block or a single-statement body
        if self.current.type == TokenType.LBRACE:
            self.expect(TokenType.LBRACE)

            while self.current.type != TokenType.RBRACE:
                body.append(self.statement())

            self.expect(TokenType.RBRACE)
        else:
            # If EOF, give a clearer error than before
            if self.current.type == TokenType.EOF:
                raise Exception(f"Syntax Error: expected {TokenType.LBRACE} or statement, got {self.current.type}")
            # single statement as body
            body.append(self.statement())

        if_node = self.add_parse_tree(
            self.current_tree_parent,
            "IF"
        )

        self.add_parse_tree(
            if_node,
            "Condition",
            condition
        )

        body_node = self.add_parse_tree(
            if_node,
            "Body"
        )

        for stmt in body:
            self.add_parse_tree(
                body_node,
                stmt.__class__.__name__,
                stmt
            )

        return IfNode(condition, body)
    
    # =========================
    # WHILE
    # =========================

    def while_statement(self):

        self.expect(TokenType.SALILA)

        condition = self.condition()

        body = []

        self.expect(TokenType.LBRACE)

        while self.current.type != TokenType.RBRACE:
            body.append(self.statement())

        self.expect(TokenType.RBRACE)

        while_node = self.add_parse_tree(
            self.current_tree_parent,
            "WHILE"
        )

        self.add_parse_tree(
            while_node,
            "Condition",
            condition
        )

        body_node = self.add_parse_tree(
            while_node,
            "Body"
        )

        for stmt in body:
            self.add_parse_tree(
                body_node,
                stmt.__class__.__name__,
                stmt
            )

        return WhileNode(condition, body)
    
    # =========================
    # FOR
    # =========================

    def for_statement(self):

        self.expect(TokenType.KEUR)

        # nama variabel loop
        variable = self.current.value
        self.expect(TokenType.IDENTIFIER)

        # keyword "dina"
        self.expect(TokenType.DINA)

        # rentang
        self.expect(TokenType.RENTANG)

        self.expect(TokenType.LPAREN)

        args = []

        if self.current.type != TokenType.RPAREN:

            args.append(self.expression())

            while self.current.type == TokenType.COMMA:
                self.expect(TokenType.COMMA)
                args.append(self.expression())

        self.expect(TokenType.RPAREN)

        self.expect(TokenType.LBRACE)

        body = []

        while self.current.type != TokenType.RBRACE:
            body.append(self.statement())

        self.expect(TokenType.RBRACE)

        # =====================
        # Parse Tree
        # =====================

        for_tree = self.add_parse_tree(
            self.current_tree_parent,
            "FOR"
        )

        self.add_parse_tree(
            for_tree,
            "VARIABLE",
            variable
        )

        range_tree = self.add_parse_tree(
            for_tree,
            "RANGE"
        )

        for arg in args:
            self.add_parse_tree(
                range_tree,
                "ARG",
                arg
            )

        body_tree = self.add_parse_tree(
            for_tree,
            "BODY"
        )

        for stmt in body:
            self.add_parse_tree(
                body_tree,
                stmt.__class__.__name__
            )

        iterable = CallNode(
            "rentang",
            args
        )

        return ForNode(
            variable,
            iterable,
            body
        )

    # =========================
    # FUNCTION DEFINITION
    # =========================

    def function_definition(self):

        self.expect(TokenType.GAWE)

        # nama fungsi
        name = self.current.value
        self.expect(TokenType.IDENTIFIER)

        # (
        self.expect(TokenType.LPAREN)

        params = []

        if self.current.type != TokenType.RPAREN:

            while True:

                params.append(self.current.value)

                self.expect(TokenType.IDENTIFIER)

                if self.current.type == TokenType.COMMA:
                    self.expect(TokenType.COMMA)
                else:
                    break

        # )
        self.expect(TokenType.RPAREN)

        # {
        self.expect(TokenType.LBRACE)

        body = []

        while self.current.type != TokenType.RBRACE:
            body.append(self.statement())

        self.expect(TokenType.RBRACE)

        # =====================
        # Parse Tree
        # =====================

        func_tree = self.add_parse_tree(
            self.current_tree_parent,
            "Function"
        )

        old_parent = self.current_tree_parent
        self.current_tree_parent = func_tree

        self.add_parse_tree(
            func_tree,
            "NAME",
            name
        )

        param_tree = self.add_parse_tree(
            func_tree,
            "PARAMETERS"
        )

        for p in params:
            self.add_parse_tree(
                param_tree,
                "PARAM",
                p
            )

        #=====================
        # BODY
        #=====================

        body_tree = self.add_parse_tree(
            func_tree,
            "BODY"
        )

        for stmt in body:

            if isinstance(stmt, ReturnNode):

                ret = self.add_parse_tree(
                    body_tree,
                    "RETURN"
                )

                self.add_parse_tree(
                    ret,
                    "VALUE",
                    stmt.value
                )

            else:

                self.add_parse_tree(
                    body_tree,
                    stmt.__class__.__name__
                )

        self.current_tree_parent = old_parent

        return FunctionNode(
            name,
            params,
            body
        )

    # =========================
    # ELSE
    # =========================

    def else_statement(self):
        self.expect(TokenType.SANESNA)

        self.expect(TokenType.LBRACE)

        body = []
        while self.current.type != TokenType.RBRACE:
            body.append(self.statement())

        self.expect(TokenType.RBRACE)

        return ElseNode(body)

    # =========================
    # FUNCTION CALL
    # =========================

    def function_call(self):

        self.expect(TokenType.NGOMONG)
        self.expect(TokenType.LPAREN)

        args = []

        if self.current.type != TokenType.RPAREN:

            args.append(self.expression())

            while self.current.type == TokenType.COMMA:
                self.expect(TokenType.COMMA)
                args.append(self.expression())

        self.expect(TokenType.RPAREN)

        call_node = self.add_parse_tree(
            self.current_tree_parent,
            "Function Call"
        )

        self.add_parse_tree(
            call_node,
            "NAME",
            "ngomong"
        )

        for arg in args:
            self.add_parse_tree(
                call_node,
                "ARG",
                arg
            )

        return CallNode("ngomong", args)

    # =========================
    # CONDITION (FIXED)
    # =========================

    def condition(self):

        self.expect(TokenType.LPAREN)

        node = self.comparison()

        self.expect(TokenType.RPAREN)

        return node

    # =========================
    # EXPRESSION
    # =========================

    def expression(self):
        return self.comparison()


    # =========================
    # COMPARISON
    # =========================

    def comparison(self):
        node = self.addition()

        while self.current.type in (
            TokenType.GREATER,
            TokenType.LESS,
            TokenType.GREATER_EQUAL,
            TokenType.LESS_EQUAL,
            TokenType.EQUAL,
            TokenType.NOT_EQUAL,
        ):
            op = self.current.type
            self.advance()

            right = self.addition()
            node = BinaryOpNode(node, op, right)

        return node


    # =========================
    # ADDITION
    # =========================

    def addition(self):
        node = self.multiplication()

        while self.current.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):
            op = self.current.type
            self.advance()

            right = self.multiplication()
            node = BinaryOpNode(node, op, right)

        return node


    # =========================
    # MULTIPLICATION
    # =========================

    def multiplication(self):
        node = self.factor()

        while self.current.type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
            TokenType.MODULO,
        ):
            op = self.current.type
            self.advance()

            right = self.factor()
            node = BinaryOpNode(node, op, right)

        return node


    # =========================
    # FACTOR
    # =========================

    def factor(self):
        token = self.current

        # NUMBER
        if token.type == TokenType.NUMBER:
            self.advance()
            return token.value

        # STRING
        if token.type == TokenType.STRING:
            self.advance()
            return StringNode(token.value)

        # BOOLEAN
        if token.type in (
            TokenType.ENYA,
            TokenType.HENTEU,
        ):
            self.advance()
            return token.value
        
        # ARRAY
        if token.type == TokenType.LBRACKET:

            self.expect(TokenType.LBRACKET)

            elements = []

            if self.current.type != TokenType.RBRACKET:

                elements.append(self.expression())

                while self.current.type == TokenType.COMMA:

                    self.expect(TokenType.COMMA)
                    elements.append(self.expression())

            self.expect(TokenType.RBRACKET)

            return ArrayNode(elements)

        # IDENTIFIER / FUNCTION CALL
        if token.type == TokenType.IDENTIFIER:

            name = token.value
            self.advance()

            # function call
            if self.current.type == TokenType.LPAREN:

                self.expect(TokenType.LPAREN)

                args = []

                if self.current.type != TokenType.RPAREN:

                    args.append(self.expression())

                    while self.current.type == TokenType.COMMA:
                        self.expect(TokenType.COMMA)
                        args.append(self.expression())

                self.expect(TokenType.RPAREN)

                return CallNode(name, args)


            # Array Index

            if self.current.type == TokenType.LBRACKET:

                self.expect(TokenType.LBRACKET)

                index = self.expression()

                self.expect(TokenType.RBRACKET)

                return IndexNode(
                    name,
                    index
                )
            
            # variable
            return name

        # ( expression )
        if token.type == TokenType.LPAREN:
            self.advance()

            node = self.expression()

            self.expect(TokenType.RPAREN)

            return node

        raise Exception(f"Invalid factor: {token.type}")
    
    # =========================
    # RETURN
    # =========================

    def return_statement(self):

        self.expect(TokenType.BALIKKEUN)

        value = self.expression()

        return ReturnNode(value)