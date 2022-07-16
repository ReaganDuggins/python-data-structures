class DoubleLinkList:
    def __init__(self, head = None):
        self.head = head

    def add(self, new_node):
        self.head = new_node