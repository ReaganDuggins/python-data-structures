class DoubleLinkList:
    def __init__(self, head = None):
        self.head = head
        self.tail = None

    def add_tail(self, new_node):
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

    def add_head(self, new_node):
        if self.head == None:
            self.head = new_node
            return
        if self.tail == None:
            self.tail = self.head
            self.head = new_node
            self.tail.previous = self.head
            self.head.next = self.tail
            return
        
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node