from data_structures.linked_list.DoubleLinkList import DoubleLinkList


class Stack(DoubleLinkList):
    def __init__(self, head = None):
        super().__init__()
        self.head = head
    
    def push(self, new_node):
        super().add_head(new_node)

    def pop(self):
        if self.head == None:
            return None
        popped = self.head.value
        self.remove(popped)
        return popped
