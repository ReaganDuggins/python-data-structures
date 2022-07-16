from tokenize import Double
import unittest

from data_structures.linked_list.DoubleLinkList import DoubleLinkList
from data_structures.linked_list.Node import Node

class TestDoubleLinkInit(unittest.TestCase):
    def test_init_empty_list(self):
        list = DoubleLinkList()
        self.assertEqual(list.head, None)
        self.assertEqual(list.size, 0)


    def test_init_with_head(self):
        list = DoubleLinkList("bob")
        self.assertEqual(list.head, "bob")
        self.assertEqual(list.size, 1)


class TestDoubleLinkAddTail(unittest.TestCase):
    def test_add_node_to_empty_list(self):
        list = DoubleLinkList()
        first_node = Node(50)

        list.add_tail(first_node)
        self.assertEqual(list.head, first_node, 'first node in list not properly added')
        self.assertEqual(list.size, 1)

    def test_add_second_node_to_list(self):
        list = DoubleLinkList()
        list.add_tail(Node('bob'))

        second_node = Node('jim')
        list.add_tail(second_node)

        self.assertEqual(list.head.value, 'bob', 'head was overwritten when adding second node')
        self.assertEqual(list.tail.value, 'jim', 'tail not properly set')
        self.assertEqual(list.head.next.value, 'jim', 'head.next is not tail')
        self.assertEqual(list.tail.previous.value, 'bob', 'tail.previoius is not head')
        self.assertEqual(list.size, 2)

    def test_add_more_nodes_to_list(self):
        list = DoubleLinkList()
        list.add_tail(Node(4))
        list.add_tail(Node(8))

        third_node = Node(-3)
        list.add_tail(third_node)

        self.assertEqual(list.head.value, 4, 'head was overwritten when adding third node')
        self.assertEqual(list.tail.value, -3, 'new node not set to be tail')
        self.assertEqual(list.head.next.value, 8, 'overwrote tail instead of adding to end')
        self.assertEqual(list.tail.previous.value, 8, 'new node overwrote tail')
        self.assertEqual(list.size, 3)

        
class TestDoubleLinkAddHead(unittest.TestCase):
    def test_add_node_to_empty_list(self):
        list = DoubleLinkList()
        first_node = Node(50)

        list.add_head(first_node)
        self.assertEqual(list.head, first_node, 'first node in list not properly added')
        self.assertEqual(list.size, 1)

    def test_add_second_node_to_list(self):
        list = DoubleLinkList()
        list.add_head(Node('bob'))

        second_node = Node('jim')
        list.add_head(second_node)

        self.assertEqual(list.head.value, 'jim', 'head was not overwritten when adding second node')
        self.assertEqual(list.tail.value, 'bob', 'tail not properly set')
        self.assertEqual(list.head.next.value, 'bob', 'head.next is not tail')
        self.assertEqual(list.tail.previous.value, 'jim', 'tail.previoius is not head')
        self.assertEqual(list.size, 2)

    def test_add_more_nodes_to_list(self):
        list = DoubleLinkList()
        list.add_head(Node(4))
        list.add_head(Node(8))

        third_node = Node(-3)
        list.add_head(third_node)

        self.assertEqual(list.head.value, -3, 'new node not set to head')
        self.assertEqual(list.tail.value, 4, 'tail overwritten')
        self.assertEqual(list.head.next.value, 8, 'head not connected to tail')
        self.assertEqual(list.tail.previous.value, 8, 'tail not connected to head')
        self.assertEqual(list.size, 3)

class TestDoubleLinkRemove(unittest.TestCase):


    def test_remove_node_from_middle(self):
        list = DoubleLinkList()
        list.add_tail(Node(4))
        list.add_tail(Node(8))
        list.add_tail(Node(10))

        list.remove(8)

        self.assertEqual(list.head.next.value, 10, 'head does not point to tail')
        self.assertEqual(list.tail.previous.value, 4, 'tail does not point to head')
        self.assertEqual(list.size, 2)


    def test_remove_head(self):
        list = DoubleLinkList()
        list.add_tail(Node(4))
        list.add_tail(Node(8))
        list.add_tail(Node(10))

        list.remove(4)

        self.assertEqual(list.head.value, 8, 'did not change head')
        self.assertEqual(list.head.next.value, 10, 'head not linked to tail')
        self.assertEqual(list.tail.previous.value, 8, 'tail not linked to head')
        self.assertEqual(list.size, 2)


    def test_remove_tail(self):
        list = DoubleLinkList()
        list.add_tail(Node(4))
        list.add_tail(Node(8))
        list.add_tail(Node(10))

        list.remove(10)

        self.assertEqual(list.head.value, 4, 'did not change tail')
        self.assertEqual(list.tail.value, 8, 'head not linked to tail')
        self.assertEqual(list.size, 2)


class TestDoubleLinkRemoveAt(unittest.TestCase):


    def test_remove_node_from_middle(self):
        list = DoubleLinkList()
        list.add_tail(Node(4))
        list.add_tail(Node(8))
        list.add_tail(Node(10))

        list.remove_at(1)

        self.assertEqual(list.head.next.value, 10, 'head does not point to tail')
        self.assertEqual(list.tail.previous.value, 4, 'tail does not point to head')
        self.assertEqual(list.size, 2)

    def test_remove_head(self):
        list = DoubleLinkList()
        list.add_tail(Node(4))
        list.add_tail(Node(8))
        list.add_tail(Node(10))

        list.remove_at(0)

        self.assertEqual(list.head.value, 8, 'did not change head')
        self.assertEqual(list.head.next.value, 10, 'head not linked to tail')
        self.assertEqual(list.tail.previous.value, 8, 'tail not linked to head')
        self.assertEqual(list.size, 2)


    def test_remove_tail(self):
        list = DoubleLinkList()
        list.add_tail(Node(4))
        list.add_tail(Node(8))
        list.add_tail(Node(10))

        list.remove_at(2)

        self.assertEqual(list.head.value, 4, 'did not change tail')
        self.assertEqual(list.head.next.value, 8, 'head not linked to tail')
        self.assertEqual(list.tail.value, 8)
        self.assertEqual(list.tail.previous.value, 4)
        self.assertEqual(list.size, 2)



class TestDoubleLinkToString(unittest.TestCase):
    def test_print_empty_list(self):
        list = DoubleLinkList()
        
        self.assertEqual(str(list), '[]')

    def test_print_empty_list(self):
        list = DoubleLinkList()
        list.add_tail(Node(7))
        list.add_tail(Node(80))
        list.add_tail(Node(-72))
        list.add_tail(Node(0))
        
        self.assertEqual(str(list), '[7, 80, -72, 0]')

    

if __name__ == '__main__':
    unittest.main()