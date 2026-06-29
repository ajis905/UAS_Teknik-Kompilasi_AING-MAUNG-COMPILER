from token_types import TokenType
from ast_nodes import (
    AssignNode,
    BinaryOpNode,
    CallNode,
    IfNode,
    AriNode,
    ElseNode,
    WhileNode,
    FunctionNode,
    ReturnNode,
    ForNode,
    StringNode,
    ArrayNode,  
    IndexNode,
    IndexAssignNode,
)

class CodeGenerator:

    def __init__(self):
        self.code = []

    # =====================
    #       OPERATOR
    # =====================

    def get_operator(self, op):

        if hasattr(op, "name"):

            mapping = {
                "EQUAL": "==",
                "NOT_EQUAL": "!=",
                "GREATER": ">",
                "LESS": "<",
                "GREATER_EQUAL": ">=",
                "LESS_EQUAL": "<=",
                "PLUS": "+",
                "MINUS": "-",
                "MULTIPLY": "*",
                "DIVIDE": "/",
                "MODULO": "%"
            }

            return mapping.get(op.name, op.name)

        return op

    # =====================
    #       FORMAT VALUE
    # =====================

    def format_value(self, value):

        if isinstance(value, bool):
            return "True" if value else "False"

        if isinstance(value, int):
            return str(value)

        if isinstance(value, str):

            # Boolean Sunda
            if value.upper() == "ENYA":
                return "True"

            if value.upper() == "HENTEU":
                return "False"

            # Identifier
            if value.isidentifier():
                return value

            # String literal
            return f'"{value}"'

        return str(value)
    
    # =====================
    #    GENERATE EXPRESSION
    # =====================

    def generate_expression(self, expr):

        # =====================
        # ARRAY
        # =====================

        if isinstance(expr, ArrayNode):

            elements = []

            for element in expr.elements:
                elements.append(
                    self.generate_expression(element)
                )

            return "[" + ", ".join(elements) + "]"

        # =====================
        # ARRAY INDEX
        # =====================

        if isinstance(expr, IndexNode):

            array = self.generate_expression(expr.array)
            index = self.generate_expression(expr.index)

            return f"{array}[{index}]"

        # =====================
        # BINARY OPERATION
        # =====================

        if isinstance(expr, BinaryOpNode):

            left = self.generate_expression(expr.left)
            right = self.generate_expression(expr.right)

            op = self.get_operator(expr.op)

            return f"({left} {op} {right})"

        # =====================
        # STRING
        # =====================

        if isinstance(expr, StringNode):
            return f'"{expr.value}"'

        # =====================
        # FUNCTION CALL
        # =====================

        if isinstance(expr, CallNode):

            args = [
                self.generate_expression(arg)
                for arg in expr.args
            ]

            # built-in input
            if expr.name == "nanya":

                if len(args) == 0:
                    return "input()"

                return f"input({args[0]})"

            # built-in len
            if expr.name == "panjang":
                return f"len({args[0]})"

            # built-in range
            if expr.name == "rentang":
                return f"range({', '.join(args)})"

            # user-defined function
            return f"{expr.name}({', '.join(args)})"

        # =====================
        # DEFAULT
        # =====================

        return self.format_value(expr)
    

    # =====================
    #       GENERATE
    # =====================

    def generate(self, ast):

        self.code = []

        for node in ast:
            self.visit(node)

        python_code = "\n".join(self.code)

        with open("generated.py", "w", encoding="utf-8") as f:
            f.write(python_code)

        return python_code

    # =====================
    #       VISIT
    # =====================

    def visit(self, node):

        # =====================
        #       ASSIGNMENT
        # =====================

        if isinstance(node, AssignNode):

            value = self.generate_expression(node.value)

            self.code.append(
                f"{node.name} = {value}"
            )

        # =====================
        # ARRAY INDEX ASSIGNMENT
        # =====================

        elif isinstance(node, IndexAssignNode):

            array = self.generate_expression(node.array)
            index = self.generate_expression(node.index)
            value = self.generate_expression(node.value)

            self.code.append(
                f"{array}[{index}] = {value}"
            )

        # =====================
        #       FUNCTION CALL
        # =====================

        elif isinstance(node, CallNode):

            # Built-in print
            if node.name == "ngomong":

                arg = self.generate_expression(node.args[0])

                self.code.append(
                    f"print({arg})"
                )

            elif node.name == "panjang":

                arg = self.generate_expression(node.args[0])

                self.code.append(
                    f"len({arg})"
    )

            # User-defined function
            else:

                args = []

                for arg in node.args:
                    args.append(
                        self.generate_expression(arg)
                    )

                self.code.append(
                    f"{node.name}({', '.join(args)})"
                )

        # =====================
        #       IF
        # =====================

        elif isinstance(node, IfNode):

            condition = node.condition

            op = self.get_operator(condition.op)

            left_expr = self.generate_expression(condition.left)
            right_expr = self.generate_expression(condition.right)

            self.code.append(
                f"if {left_expr} {op} {right_expr}:"
            )

            old = self.code
            self.code = []

            for stmt in node.body:
                self.visit(stmt)

            body = self.code
            self.code = old

            for line in body:
                self.code.append("    " + line)

        # =====================
        #       ELIF
        # =====================

        elif isinstance(node, AriNode):

            condition = node.condition

            op = self.get_operator(condition.op)

            left_expr = self.generate_expression(condition.left)
            right_expr = self.generate_expression(condition.right)

            self.code.append(
                f"elif {left_expr} {op} {right_expr}:"
            )

            old = self.code
            self.code = []

            for stmt in node.body:
                self.visit(stmt)

            body = self.code
            self.code = old

            for line in body:
                self.code.append("    " + line)

        # =====================
        #       ELSE
        # =====================

        elif isinstance(node, ElseNode):

            self.code.append("else:")

            old = self.code
            self.code = []

            for stmt in node.body:
                self.visit(stmt)

            body = self.code
            self.code = old

            for line in body:
                self.code.append("    " + line)

        # =====================
        #       fUNCTION
        # =====================
    
        elif isinstance(node, FunctionNode):

            params = ", ".join(node.params)

            self.code.append(
                f"def {node.name}({params}):"
            )

            old = self.code
            self.code = []

            for stmt in node.body:
                self.visit(stmt)

            body = self.code
            self.code = old

            if not body:
                self.code.append("    pass")
            else:
                for line in body:
                    self.code.append("    " + line)

        # =====================
        #       WHILE
        # =====================

        elif isinstance(node, WhileNode):

            condition = node.condition

            op = self.get_operator(condition.op)

            left_expr = self.generate_expression(condition.left)
            right_expr = self.generate_expression(condition.right)

            self.code.append(
                f"while {left_expr} {op} {right_expr}:"
            )

            old = self.code
            self.code = []

            for stmt in node.body:
                self.visit(stmt)

            body = self.code
            self.code = old

            for line in body:
                self.code.append("    " + line)

        # =====================
        #       FOR
        # =====================

        elif isinstance(node, ForNode):

            iterable = self.generate_expression(node.iterable)

            self.code.append(
                f"for {node.variable} in {iterable}:"
            )

            old = self.code
            self.code = []

            for stmt in node.body:
                self.visit(stmt)

            body = self.code
            self.code = old

            if len(body) == 0:
                self.code.append("    pass")
            else:
                for line in body:
                    self.code.append("    " + line)

        # =====================
        #       RETURN  
        # =====================
    
        elif isinstance(node, ReturnNode):

            value = self.generate_expression(node.value)

            self.code.append(
                f"return {value}"
            )