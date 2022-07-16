import unittest

from data_structures.linked_list.DoubleLinkList import DoubleLinkList
from data_structures.linked_list.Node import Node

class TestDoubleLinkInit(unittest.TestCase):
    def test_init_empty_list(self):
        list = DoubleLinkList()
        self.assertEqual(list.head, None)

    def test_init_with_head(self):
        list = DoubleLinkList("bob")
        self.assertEqual(list.head, "bob")

class TestDoubleLinkAdd(unittest.TestCase):
    def test_add_node_to_empty_list(self):
        list = DoubleLinkList()
        first_node = Node(50)

        list.add(first_node)
        self.assertEqual(list.head, first_node, 'first node in list not properly added')

    def test_add_second_node_to_list(self):
        list = DoubleLinkList()
        list.add(Node('bob'))

        second_node = Node('jim')
        list.add(second_node)

        self.assertEqual(list.head.value, 'bob', 'head was overwritten when adding second node')
        self.assertEqual(list.tail.value, 'jim', 'tail not properly set')
        self.assertEqual(list.head.next.value, 'jim', 'head.next is not tail')
        self.assertEqual(list.tail.previous.value, 'bob', 'tail.previoius is not head')

if __name__ == '__main__':
    unittest.main()