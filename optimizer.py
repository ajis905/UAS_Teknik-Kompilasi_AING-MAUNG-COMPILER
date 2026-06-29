from ast_nodes import IfNode

# =====================
# OPTIMIZER
# =====================

class Optimizer:

    def optimize(self, ast):

       # print("[Optimization] Teu aya optimasi nu dipake.")

        return ast

    def visit(self, node):

        if isinstance(node, IfNode):

            cond = node.condition

            # Constant Folding sederhana
            if (
                isinstance(cond.left, str)
                and isinstance(cond.right, str)
            ):

                if cond.op.name == "EQUAL":

                    if cond.left != cond.right:

                        print(
                            "[Optimization] Blok lamun dihapus sabab salawasna FALSE"
                        )

                        return None

        return node