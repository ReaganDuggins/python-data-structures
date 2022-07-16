class DoubleLinkList:
    def __init__(self, head = None):
        self.head = head
        self.tail = None
        self.size = 0
        if head:
            self.size += 1

    def add_tail(self, new_node):
        if self.head == None:
            self.head = new_node
            self.size += 1
            return
        if self.tail == None:
            self.tail = new_node
            self.tail.previous = self.head
            self.head.next = self.tail
            self.size += 1
            return
        
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        self.size += 1

    def add_head(self, new_node):
        if self.head == None:
            self.head = new_node
            self.size += 1
            return
        if self.tail == None:
            self.tail = self.head
            self.head = new_node
            self.tail.previous = self.head
            self.head.next = self.tail
            self.size += 1
            return
        
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove(self, remove_me):
        if self.head.value == remove_me:
            self.head = self.head.next
            self.size -= 1
            return

        if self.tail.value == remove_me:
            self.tail = self.tail.previous
            self.size -= 1
            return

        current = self.head
        while(current != None):
            if current.value == remove_me:
                prev = current.previous
                nex = current.next
                if prev:
                    prev.next = nex
                if nex:
                    nex.previous = prev
                current = None
                self.size -= 1
                return
            current = current.next

    def remove_at(self, removal_index):
        if removal_index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        if removal_index == self.size - 1:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return

        current = self.head
        current_index = 0
        while(current != None):
            if current_index == removal_index:
                prev = current.previous
                nex = current.next
                if prev:
                    prev.next = nex
                if nex:
                    nex.previous = prev
                current = None
                self.size -= 1
                return
            current = current.next
            current_index += 1

    def __str__(self):
        before = '['
        current = self.head
        while current:
            before += str(current.value) + ', '
            current = current.next
        before = before[0:(len(before)-2)]
        before += ']'
        return before