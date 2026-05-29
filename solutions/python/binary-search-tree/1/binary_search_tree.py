"""Binary tree"""
class TreeNode:
    """Tree node"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

class BinarySearchTree:
    """Binary tree"""
    def __init__(self, tree_data):
        self.value = None
        if len(tree_data) >0:
            root = tree_data[0]
            self.value = TreeNode(root)
            for number in tree_data[1:]:
                new_node = TreeNode(number)
                node = self.value
                while True:
                    if number <= node.data:
                        if node.left is None:
                            node.left = new_node
                            break
                        node = node.left
                    else:
                        if node.right is None:
                            node.right = new_node
                            break
                        node = node.right          

    def data(self):
        return self.value

    def sorted_data(self):
        result = []
        stack = []
        node = self.value
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.data)
            node = node.right
        return result
