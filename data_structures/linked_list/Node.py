class Node:
    def __init__(self, value = None, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous
    
    def __str__(self):
        if self.value:
            return str(self.value)
        return ''