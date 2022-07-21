from msilib.schema import Binary
import unittest

from data_structures.trees.BinarySearchTree import BinarySearchTree
from data_structures.trees.Node import Node

class TestBSTInit(unittest.TestCase):
    def test_init_empty(self):
        tree = BinarySearchTree()

        self.assertEqual(tree.root, None)
        self.assertEqual(tree.size, 0)

    def test_init_with_root(self):
        tree = BinarySearchTree(4)

        self.assertEqual(tree.root.value, 4)
        self.assertEqual(tree.size, 1)

class TestBSTAdd(unittest.TestCase):
    def test_add_first_becomes_root(self):
        tree = BinarySearchTree()

        tree.add('bob')

        self.assertEqual(tree.root.value, 'bob')

    def test_smaller_goes_left(self):
        tree = BinarySearchTree()

        tree.add(10)
        tree.add(3)

        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 3)

    def test_larger_goes_right(self):
        tree = BinarySearchTree()

        tree.add(10)
        tree.add(13)

        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.right.value, 13)

    def test_keep_adding_to_left(self):
        tree = BinarySearchTree()

        tree.add(50)
        tree.add(30)
        tree.add(20)
        tree.add(10)

        self.assertEqual(tree.root.value, 50)
        self.assertEqual(tree.root.left.value, 30)
        self.assertEqual(tree.root.left.left.value, 20)
        self.assertEqual(tree.root.left.left.left.value, 10)

    def test_keep_adding_to_right(self):
        tree = BinarySearchTree()

        tree.add(10)
        tree.add(20)
        tree.add(30)
        tree.add(50)

        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.right.value, 20)
        self.assertEqual(tree.root.right.right.value, 30)
        self.assertEqual(tree.root.right.right.right.value, 50)

    def test_keep_adding_alternating(self):
        tree = BinarySearchTree()

        tree.add(50)
        tree.add(20)
        tree.add(15)
        tree.add(25)

        self.assertEqual(tree.root.value, 50)
        self.assertEqual(tree.root.left.value, 20)
        self.assertEqual(tree.root.left.left.value, 15)
        self.assertEqual(tree.root.left.right.value, 25)

class TestBSTRemove(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.add(33)
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)
        self.tree.add(50)
        self.tree.add(40)
        self.tree.add(70)

    def test_remove_from_empty_tree_not_crash(self):
        tree = BinarySearchTree()
        notbob = tree.remove('bob')

        self.assertEqual(notbob, None)

    def test_remove_root_when_it_is_only_node(self):
        tree = BinarySearchTree()
        tree.add(5)

        removed = tree.remove(5)

        self.assertEqual(removed, 5)
        self.assertIsNone(tree.root)

    def test_remove_root_with_only_left_child(self):
        tree = BinarySearchTree()
        tree.add(10)
        tree.add(3)

        removed = tree.remove(10)

        self.assertEqual(removed, 10)
        self.assertEqual(tree.root.value, 3)
        self.assertIsNone(tree.root.left)

    def test_remove_root_with_only_right_child(self):
        tree = BinarySearchTree()
        tree.add(10)
        tree.add(20)

        removed = tree.remove(10)

        self.assertEqual(removed, 10)
        self.assertEqual(tree.root.value, 20)
        self.assertIsNone(tree.root.right)