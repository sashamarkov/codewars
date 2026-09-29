def rotate_left(tree):
    if not tree or not tree.right:
        return tree
    new_tree = tree.right
    tree.right = new_tree.left
    new_tree.left = tree
    return new_tree
​
def rotate_right(tree):
    if not tree or not tree.left:
        return tree
    new_tree = tree.left
    tree.left = new_tree.right
    new_tree.right = tree
    return new_tree