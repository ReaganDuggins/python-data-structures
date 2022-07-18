import unittest

from data_structures.linked_list.Node import Node

class TestNodeInit(unittest.TestCase):
    def test_all_instance_vars_exist(self):
        node = Node(43, 'next', 'prev')
        self.assertEqual(node.value, 43)
        self.assertEqual(node.next, 'next')
        self.assertEqual(node.previous, 'prev')

class TestNodeToString(unittest.TestCase):
    def test_empty_node_is_empty_string(self):
        node = Node()

        self.assertEqual(str(node), '')

    def test_node_prints_value(self):
        node = Node('some node value')

        self.assertEqual(str(node), 'some node value')

    