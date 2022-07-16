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

    def remove(self, remove_me):
        if self.head.value == remove_me:
            self.head = self.head.next
            return

        if self.tail.value == remove_me:
            self.tail = self.tail.previous

        current = self.head
        while(self.head != None):
            if current.value == remove_me:
                prev = current.previous
                nex = current.next
                if prev:
                    prev.next = nex
                if nex:
                    nex.previous = prev
                current = None
                return
            current = current.next

    def __str__(self):
        before = '['
        current = self.head
        while current:
            before += str(current.value) + ', '
            current = current.next
        before = before[0:(len(before)-2)]
        before += ']'
        return before