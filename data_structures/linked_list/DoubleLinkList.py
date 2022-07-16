class DoubleLinkList:
    def __init__(self, head = None):
        self.head = head
        self.tail = None

    def add(self, new_node):
        if self.head == None:
            self.head = new_node
            return
        if self.tail == None:
            self.tail = new_node
            self.tail.previous = self.head
            self.head.next = self.tail
            return
        
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node