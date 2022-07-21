from data_structures.trees.Node import Node

class BinarySearchTree:
    def __init__(self, root = None):
        self.size = 0
        self.root = None
        if root:
            self.size += 1
            self.root = Node(root)

    def add(self, add_me):
        new_node = Node(add_me)
        if self.root == None:
            self.root = new_node
            return
        
        current = self.root

        while current != None:
            if new_node.value < current.value:
                if current.left == None:
                    current.left = new_node
                    self.size += 1
                    return
                current = current.left
                continue
            
            if current.right == None:
                current.right = new_node
                self.size += 1
                return
            current = current.right
    
    def remove(self, value):
        if self.root == None:
            return None
        if value == self.root.value:
            removed = self.root.value
            if BinarySearchTree.has_no_children(self.root):
                self.root = None
                return removed
            if BinarySearchTree.has_only_left_child(self.root):
                self.root = self.root.left
                return removed
            if BinarySearchTree.has_only_right_child(self.root):
                self.root = self.root.right
                return removed

    def has_only_left_child(node):
        return node.left != None and node.right == None

    def has_only_right_child(node):
        return node.left == None and node.right != None

    def has_both_children(node):
        return node.left != None and node.right != None

    def has_no_children(node):
        return node.left == None and node.right == None
            
            
        
        

        


    