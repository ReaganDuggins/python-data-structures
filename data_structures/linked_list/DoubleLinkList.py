from data_structures.linked_list.Node import Node

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

    def add_after_index(self, new_node, index):
        if self.head == None:
            self.head = new_node
            self.size += 1
            return

        if index < 0:
            new_node.next = self.head
            self.head = new_node
            self.head.next.previous = self.head
            self.size += 1
            if self.tail == None:
                self.tail = self.head.next
            return

        if index >= self.size:
            if self.tail:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
                self.size += 1
                return
            self.tail = new_node
            self.head.next = self.tail
            self.tail.previous = self.head
            self.size += 1
            return

        before = self.head
        current = 0

        while before:
            if current == index:
                after = before.next
                if after:
                    after.previous = new_node
                new_node.next = after
                new_node.previous = before
                before.next = new_node
                self.size += 1
                return
            before = before.next
            current += 1
            

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

    def reverse(self):
        reversed_list = DoubleLinkList()
        if self.size < 1:
            return reversed_list
        if self.size == 1:
            reversed_list.add_head(Node(self.head.value))
            return reversed_list

        current = self.tail
        while current:
            node = Node(current.value)
            reversed_list.add_tail(node)
            current = current.previous
        
        return reversed_list


    def __str__(self):
        before = '['
        current = self.head
        while current:
            before += str(current.value) + ', '
            current = current.next
        if len(before) > 2:
            before = before[0:(len(before)-2)]
        before += ']'
        return before