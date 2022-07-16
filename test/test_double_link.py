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

    def test_add_more_nodes_to_list(self):
        list = DoubleLinkList()
        list.add(Node(4))
        list.add(Node(8))

        third_node = Node(-3)
        list.add(third_node)

        self.assertEqual(list.head.value, 4, 'head was overwritten when adding third node')
        self.assertEqual(list.tail.value, -3, 'new node not set to be tail')
        self.assertEqual(list.head.next.value, 8, 'overwrote tail instead of adding to end')
        self.assertEqual(list.tail.previous.value, 8, 'new node overwrote tail')

        print(list.head.value, list.head.next.value, list.head.next.next.value, list.tail.value, list.tail.previous.value, list.tail.previous.previous.value)
        

if __name__ == '__main__':
    unittest.main()