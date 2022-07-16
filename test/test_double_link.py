import unittest

from data_structures.linked_list.double_link_list import DoubleLinkList

print('YO')

class TestDoubleLinkInit(unittest.TestCase):
    def test_init_empty_list(self):
        list = DoubleLinkList()
        self.assertEqual(list.head, None)

if __name__ == '__main__':
    unittest.main()