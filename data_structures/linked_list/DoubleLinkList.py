class DoubleLinkList:
    def __init__(self, head = None):
        self.head = head
        self.tail = None

    def add(self, new_node):
        if self.head == None:
            self.head = new_node
            return
        self.tail = new_node
        self.tail.previous = self.head
        self.head.next = self.tail