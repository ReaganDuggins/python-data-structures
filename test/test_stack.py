import unittest

from data_structures.linked_list.Stack import Stack
from data_structures.linked_list.Node import Node

class TestStackInit(unittest.TestCase):
    def test_default_constructor(self):
        stack = Stack()
        self.assertNotEqual(stack, None)
        self.assertEqual(stack.head, None)

    def test_construct_with_head(self):
        my_head = Node(4)
        stack = Stack(my_head)

        self.assertEqual(stack.head.value, 4)

class TestStackPush(unittest.TestCase):
    def test_push_first(self):
        stack = Stack()
        stack.push(Node('blah'))

        self.assertEqual(stack.head.value, 'blah')

    def test_push_second(self):
        stack = Stack()
        stack.push(Node('blah'))
        stack.push(Node('blee'))

        self.assertEqual(stack.head.value, 'blee')
        self.assertEqual(stack.head.next.value, 'blah')

    def test_push_multiplel(self):
        stack = Stack()
        stack.push(Node('blah'))
        stack.push(Node('blee'))
        stack.push(Node('blurf'))
        stack.push(Node('bleedle'))
        stack.push(Node('blorp'))

        self.assertEqual(stack.head.value, 'blorp')
        self.assertEqual(stack.head.next.next.next.next.value, 'blah')

class TestStackPop(unittest.TestCase):
    def test_pop_empty_returns_none(self):
        stack = Stack()

        self.assertEqual(stack.pop(), None)

    def test_pop_only_element_in_stack(self):
        stack = Stack()
        stack.push(Node('yo'))

        popped = stack.pop()

        self.assertEqual(popped, 'yo')
        self.assertIsNone(stack.head)

    def test_pop_only_removes_head(self):
        stack = Stack()
        stack.push(Node(43))
        stack.push(Node(10))
        stack.push(Node(8))
        stack.push(Node(128512))

        popped = stack.pop()
        self.assertEqual(popped, 128512)
        self.assertEqual(stack.head.value, 8)

class TestStackPeek(unittest.TestCase):
    def test_peek_empty_is_none(self):
        stack = Stack()

        self.assertIsNone(stack.peek())

    def test_peek_not_remove_head(self):
        stack = Stack()
        stack.push(Node(18))

        peeked = stack.peek()
        self.assertEqual(peeked, stack.head.value)