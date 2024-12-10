from anytree import Node, RenderTree

def visualize_parse_tree(parse_tree):
    root = Node("Root")
    build_tree(parse_tree, root)
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

def build_tree(parse_tree, parent_node):
    if isinstance(parse_tree, tuple):
        operator = parse_tree[0]
        left = parse_tree[1]
        right = parse_tree[2]

        current_node = Node(operator, parent=parent_node)

        build_tree(left, current_node)
        build_tree(right, current_node)
    else:
        Node(str(parse_tree), parent=parent_node)

if __name__ == "__main__":
    parsed_result = ('+', 3, ('*', 5, ('-', 10, 2)))  
    visualize_parse_tree(parsed_result)
