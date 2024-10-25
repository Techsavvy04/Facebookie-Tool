class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
class tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        new_node = None(data)
        if self.root is None:
            self.root = new_node
        else:
            