from Node import Node

class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def __repr__(self):
        return f"<BST: {self.root}"
    
    def add_node(self, value):
        pass

    def search(self,value):
        pass

    def get_min(self):
        pass

    def get_max(self):
        pass

    def print_sorted(self):
        pass

bst = BinarySearchTree(100)

print(bst)
