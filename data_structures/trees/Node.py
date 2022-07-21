class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        if self.value:
            return str(self.value)
        return ''