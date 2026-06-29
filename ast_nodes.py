
class ASTNode:
    pass


class AssignNode(ASTNode):
    def __init__(self, name, value, value_type):
        self.name = name
        self.value = value
        self.value_type = value_type

    def __repr__(self):
        return (
            f"AssignNode(name={self.name}, "
            f"value={self.value}, "
            f"type={self.value_type})"
        )

class CallNode(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"CallNode(name={self.name}, args={self.args})"

class IfNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"IfNode(condition={self.condition}, body={self.body})"
    
class AriNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"AriNode(condition={self.condition}, body={self.body})"

class ElseNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return f"ElseNode(body={self.body})"

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WhileNode(condition={self.condition}, body={self.body})"
    
class ForNode(ASTNode):

    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body

    def __repr__(self):
        return (
            f"ForNode("
            f"variable={self.variable}, "
            f"iterable={self.iterable}, "
            f"body={self.body})"
        )
    
class FunctionNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return (
            f"FunctionNode("
            f"name={self.name}, "
            f"params={self.params}, "
            f"body={self.body})"
        )    
    
class ReturnNode(ASTNode):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ReturnNode(value={self.value})"

class ConditionNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        op = self.op

        if hasattr(op, "value"):
            op = op.value

        return f"ConditionNode({self.left} {op} {self.right})"

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        op = self.op

        if hasattr(op, "name"):
            op = op.name

        return f"BinaryOpNode({self.left} {op} {self.right})"
    
class StringNode(ASTNode):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'StringNode("{self.value}")'
 
class ArrayNode(ASTNode):

    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"ArrayNode(elements={self.elements})"
    
class IndexNode(ASTNode):

    def __init__(self, array, index):
        self.array = array
        self.index = index

    def __repr__(self):
        return (
            f"IndexNode(array={self.array}, "
            f"index={self.index})"
        )
    
class IndexAssignNode(ASTNode):

    def __init__(self, array, index, value):
        self.array = array
        self.index = index
        self.value = value

    def __repr__(self):
        return (
            f"IndexAssignNode("
            f"array={self.array}, "
            f"index={self.index}, "
            f"value={self.value})"
        )