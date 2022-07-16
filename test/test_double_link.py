import unittest

from data_structures.linked_list.double_link_list import DoubleLinkList

class TestDoubleLinkInit(unittest.TestCase):
    def test_init_empty_list(self):
        list = DoubleLinkList()
        self.assertEqual(list.head, None)

    def test_init_with_head(self):
        list = DoubleLinkList("bob")
        self.assertEqual(list.head, "bob")

if __name__ == '__main__':
    unittest.main()