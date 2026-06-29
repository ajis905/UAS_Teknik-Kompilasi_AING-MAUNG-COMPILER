from ast import expr

from token_types import TokenType
from ast_nodes import (
    AssignNode,
    BinaryOpNode,
    CallNode,
    IfNode,
    AriNode,
    ElseNode,
    StringNode,
    WhileNode,
    FunctionNode,
    ReturnNode,
    StringNode,
    ArrayNode,
    IndexAssignNode,
)

# =====================
# SEMANTIC ANALYZER
# =====================

class SemanticAnalyzer:

    def __init__(self):
        self.symbol_table = {}
        self.function_table = {}

    def analyze(self, ast):

        for node in ast:
            self.visit(node)

    # ==========================
    # VISITOR
    # ==========================

    def visit(self, node):

        # ----------------------
        # Assignment
        # ----------------------

        if isinstance(node, AssignNode):

            self.check_expression(node.value)

            self.symbol_table[node.name] = True

        # ----------------------
        # ARRAY INDEX ASSIGNMENT
        # ----------------------

        elif isinstance(node, IndexAssignNode):

            # array harus sudah ada
            if node.array not in self.symbol_table:

                raise Exception(
                    f"Kasalahan Semantic: variabel '{node.array}' can acan dijieun."
                )

            self.check_expression(node.index)
            self.check_expression(node.value)

        # ----------------------
        # Function Call
        # ----------------------

        # ----------------------
        # IF
        # ----------------------

        elif isinstance(node, IfNode):

            self.check_expression(node.condition.left)
            self.check_expression(node.condition.right)

            for stmt in node.body:
                self.visit(stmt)

        # ----------------------
        # ELIF
        # ----------------------

        elif isinstance(node, AriNode):

            self.check_expression(node.condition.left)
            self.check_expression(node.condition.right)

            for stmt in node.body:
                self.visit(stmt)

        # ----------------------
        # ELSE
        # ----------------------

        elif isinstance(node, ElseNode):

            for stmt in node.body:
                self.visit(stmt)

        # ----------------------
        # WHILE
        # ----------------------

        elif isinstance(node, WhileNode):

            self.check_expression(node.condition.left)
            self.check_expression(node.condition.right)

            for stmt in node.body:
                self.visit(stmt)

        # ----------------------
        # FUNCTION
        # ----------------------

        elif isinstance(node, FunctionNode):

            if node.name in self.function_table:

                raise Exception(
                    f"Function '{node.name}' geus aya."
                )

            self.function_table[node.name] = node

            # simpan scope lama
            old_symbols = self.symbol_table.copy()

            # parameter dianggap sudah ada
            for param in node.params:
                self.symbol_table[param] = True

            # cek isi function
            for stmt in node.body:
                self.visit(stmt)

            # keluar dari scope function
            self.symbol_table = old_symbols

        # ----------------------
        # RETURN
        # ----------------------

        elif isinstance(node, ReturnNode):

            self.check_expression(node.value)

    # ==========================
    # Expression Checker
    # ==========================

    def check_expression(self, expr):

    # Array
        if isinstance(expr, ArrayNode):

            for element in expr.elements:
                self.check_expression(element)

            return

        if isinstance(expr, BinaryOpNode):

            self.check_expression(expr.left)
            self.check_expression(expr.right)
            return

        # Function Call
        if isinstance(expr, CallNode):

            # built-in
            if expr.name not in (
                "ngomong",
                "nanya",
                "panjang",
                "rentang",
            ):

                if expr.name not in self.function_table:
                    raise Exception(
                        f"Function '{expr.name}' teu kapanggih."
                    )

            for arg in expr.args:
                self.check_expression(arg)

            return

        if isinstance(expr, int):
            return

        if isinstance(expr, StringNode):
            return

        if isinstance(expr, bool):
            return

        if isinstance(expr, str):

            upper = expr.upper()

            # Boolean Sunda
            if upper in ("ENYA", "HENTEU"):
                return

            # String literal
            if " " in expr:
                return

            # Identifier
            if expr not in self.symbol_table:

                raise Exception(
                    f"Kasalahan Semantic: variabel '{expr}' can acan dijieun."
                )
            
    # ==========================
    # Collect Identifier
    # ==========================

    def _collect_identifiers_in_expr(self, expr):

        ids = []

        if isinstance(expr, BinaryOpNode):

            ids += self._collect_identifiers_in_expr(expr.left)
            ids += self._collect_identifiers_in_expr(expr.right)

        elif isinstance(expr, str):

            # abaikan literal string
            if " " in expr:
                return ids

            # abaikan boolean
            if expr.upper() in ("ENYA", "HENTEU"):
                return ids

            ids.append(expr)

        return ids