from token_types import TokenType
from ast_nodes import (
    AssignNode,
    BinaryOpNode,
    CallNode,
    IfNode,
    AriNode,
    ElseNode,
    WhileNode,
    ForNode,
    FunctionNode,
    ReturnNode,
    StringNode,
    ArrayNode,
    IndexAssignNode,
)

# ======================
# AST PRINTER   
# ======================

def print_ast(nodes):

    print("\n=== ABSTRACT SYNTAX TREE ===\n")

    for node in nodes:
        print_node(node)

# ======================
# PRINT NODE
# ======================

def print_node(node, indent=""):

    if isinstance(node, AssignNode):

        print(f"{indent}AssignNode")
        print(f"{indent}├── Name  : {node.name}")

        if isinstance(node.value, BinaryOpNode):

            print(f"{indent}└── Value")
            _print_binary(node.value, indent + "    ")

        elif isinstance(node.value, ArrayNode):

            print(f"{indent}└── Value")
            print_node(node.value, indent + "    ")

        else:

            print(f"{indent}└── Value : {node.value}")
            
        print()
        
    # ======================
    # INDEX ASSIGN
    # ======================    
    elif isinstance(node, IndexAssignNode):

        print(f"{indent}IndexAssignNode")
        print(f"{indent}├── Array : {node.array}")
        print(f"{indent}├── Index : {node.index}")
        print(f"{indent}└── Value : {node.value}")

        print()

    elif isinstance(node, IfNode):

        print(f"{indent}IfNode")
        print(f"{indent}├── Condition")

        cond = node.condition

        op_map = {
            TokenType.GREATER: ">",
            TokenType.LESS: "<",
            TokenType.GREATER_EQUAL: ">=",
            TokenType.LESS_EQUAL: "<=",
            TokenType.EQUAL: "==",
            TokenType.NOT_EQUAL: "!=",
        }

        op = op_map.get(cond.op, str(cond.op))

        print(f"{indent}│   ├── Left  : {cond.left}")
        print(f"{indent}│   ├── Op    : {op}")
        print(f"{indent}│   └── Right : {cond.right}")

        print(f"{indent}└── Body")

        for stmt in node.body:
            print_node(stmt, indent + "    ")

    # ======================
    # ARITHMETIC
    # ======================

    elif isinstance(node, AriNode):

        print(f"{indent}AriNode")
        print(f"{indent}├── Condition")

        cond = node.condition

        op_map = {
            TokenType.GREATER: ">",
            TokenType.LESS: "<",
            TokenType.GREATER_EQUAL: ">=",
            TokenType.LESS_EQUAL: "<=",
            TokenType.EQUAL: "==",
            TokenType.NOT_EQUAL: "!=",
        }

        op = op_map.get(cond.op, str(cond.op))

        print(f"{indent}│   ├── Left  : {cond.left}")
        print(f"{indent}│   ├── Op    : {op}")
        print(f"{indent}│   └── Right : {cond.right}")

        print(f"{indent}└── Body")

        for stmt in node.body:
            print_node(stmt, indent + "    ")

    # ======================
    # ELSE
    # ======================

    elif isinstance(node, ElseNode):

        print(f"{indent}ElseNode")
        print(f"{indent}└── Body")

        for stmt in node.body:
            print_node(stmt, indent + "    ")

    # ======================
    # WHILE
    # ======================

    elif isinstance(node, WhileNode):

        print(f"{indent}WhileNode")
        print(f"{indent}├── Condition")

        cond = node.condition

        op_map = {
            TokenType.GREATER: ">",
            TokenType.LESS: "<",
            TokenType.GREATER_EQUAL: ">=",
            TokenType.LESS_EQUAL: "<=",
            TokenType.EQUAL: "==",
            TokenType.NOT_EQUAL: "!=",
        }

        op = op_map.get(cond.op, str(cond.op))

        print(f"{indent}│   ├── Left  : {cond.left}")
        print(f"{indent}│   ├── Op    : {op}")
        print(f"{indent}│   └── Right : {cond.right}")

        print(f"{indent}└── Body")

        for stmt in node.body:
            print_node(stmt, indent + "    ")

    # ======================
    # FOR
    # ======================

    elif isinstance(node, ArrayNode):

        print(f"{indent}ArrayNode")

        for element in node.elements:

            if isinstance(element, BinaryOpNode):

                print(f"{indent}├── Element")
                _print_binary(element, indent + "│   ")

            else:

                print(f"{indent}├── {element}")

    # ======================
    # FOR node
    # ======================

    elif isinstance(node, ForNode):

        print(f"{indent}ForNode")
        print(f"{indent}├── Variable : {node.variable}")
        print(f"{indent}├── Iterable : {node.iterable}")
        print(f"{indent}└── Body")

        for stmt in node.body:
            print_node(stmt, indent + "    ")

    # ======================
    # FUNCTION node 
    # ======================

    elif isinstance(node, FunctionNode):

        print(f"{indent}FunctionNode")
        print(f"{indent}├── Name : {node.name}")

        print(f"{indent}├── Parameters")

        if node.params:

            for p in node.params:
                print(f"{indent}│   └── {p}")

        else:

            print(f"{indent}│   (none)")

        print(f"{indent}└── Body")

        for stmt in node.body:
            print_node(stmt, indent + "    ")

    # ======================
    # RETURN node
    # ======================

    elif isinstance(node, ReturnNode):

        print(f"{indent}ReturnNode")

        if isinstance(node.value, BinaryOpNode):

            print(f"{indent}└── Value")
            _print_binary(node.value, indent + "    ")

        else:

            print(f"{indent}└── Value : {node.value}")

    # ======================
    # CALL node
    # ======================

    elif isinstance(node, CallNode):

        print(f"{indent}CallNode")
        print(f"{indent}├── Name : {node.name}")

        for arg in node.args:

            if isinstance(arg, dict):
                print(f"{indent}└── Arg  : {arg['value']}")
            else:
                print(f"{indent}└── Arg  : {arg}")

        print()


# ======================
# BINARY OPERATOR
# ======================

def _print_binary(node, indent=""):

    print(f"{indent}BinaryOpNode")

    if isinstance(node.left, BinaryOpNode):

        print(f"{indent}├── Left")
        _print_binary(node.left, indent + "│   ")

    else:

        print(f"{indent}├── Left  : {node.left}")

    op_map = {
        TokenType.PLUS: "+",
        TokenType.MINUS: "-",
        TokenType.MULTIPLY: "*",
        TokenType.DIVIDE: "/",
        TokenType.MODULO: "%",
        TokenType.GREATER: ">",
        TokenType.LESS: "<",
        TokenType.GREATER_EQUAL: ">=",
        TokenType.LESS_EQUAL: "<=",
        TokenType.EQUAL: "==",
        TokenType.NOT_EQUAL: "!=",
    }

    operator = op_map.get(node.op, str(node.op))

    print(f"{indent}├── Op    : {operator}")

    if isinstance(node.right, BinaryOpNode):

        print(f"{indent}└── Right")
        _print_binary(node.right, indent + "    ")

    else:

        print(f"{indent}└── Right : {node.right}")