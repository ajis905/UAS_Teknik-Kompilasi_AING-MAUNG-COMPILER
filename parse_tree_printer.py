def print_tree(node, indent="", last=True):

    branch = "└── " if last else "├── "

    print(indent + branch + node.name)

    indent += "    " if last else "│   "

    for i, child in enumerate(node.children):
        is_last = i == len(node.children) - 1
        print_tree(child, indent, is_last)