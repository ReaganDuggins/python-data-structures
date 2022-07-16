import unittest

from data_structures.linked_list.Node import Node

class TestNodeInit(unittest.TestCase):
    def test_all_instance_vars_exist(self):
        node = Node(43, 'next', 'prev')
        self.assertEqual(node.value, 43)
        self.assertEqual(node.next, 'next')
        self.assertEqual(node.previous, 'prev')