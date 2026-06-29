print("""
========================================
      AING MAUNG COMPILER v1.0
    Basa Sunda Kasar Programming
========================================
""")

from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer
from parse_tree_printer import print_tree
from ast_printer import print_ast
from optimizer import Optimizer
from code_generator import CodeGenerator

import subprocess
import sys


def main():

    try:

        # ==========================
        # READ SOURCE
        # ==========================

        with open("sample.am", "r", encoding="utf-8") as f:
            code = f.read()

        # ==========================
        # LEXER
        # ==========================

        lexer = Lexer(code)
        tokens = lexer.tokenize()

        # ==========================
        # PARSER
        # ==========================

        parser = Parser(tokens)
        ast = parser.parse()

        print("\n=== PARSE TREE ===\n")
        print_tree(parser.parse_tree_root)

        print_ast(ast)

        # ==========================
        # OPTIMIZER
        # ==========================

        optimizer = Optimizer()
        ast = optimizer.optimize(ast)

        # ==========================
        # SEMANTIC ANALYZER
        # ==========================

        semantic = SemanticAnalyzer()
        semantic.analyze(ast)

        print("\nSemantic Analysis Berhasil!")

        # ==========================
        # CODE GENERATOR
        # ==========================

        generator = CodeGenerator()
        python_code = generator.generate(ast)

        print("\n=== GENERATED PYTHON ===\n")
        print(python_code)

        print("\nPython code disimpen kana generated.py")

        # ==========================
        # EXECUTE
        # ==========================

        print("\n=== HASIL EKSEKUSI PROGRAM ===\n")

        subprocess.run(
            [sys.executable, "generated.py"],
            check=True
        )

    except Exception as e:

        print("\n========================================")
        print("         COMPILER ERROR")
        print("========================================")
        print(e)


if __name__ == "__main__":  
    main()