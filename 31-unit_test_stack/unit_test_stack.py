'''
Stack test unit test
'''

import unittest
from stack import Stack

class StackTest (unittest.TestCase):
    '''
    Test Class for Custom Stack Class
    '''
    def test_special_stack(self):
        '''
        Method to unit test the build and functionality of Stack
        '''
        stack = Stack()
        stack.push(44)
        stack.push(52)
        stack.push(81)
        stack.push(100)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.peek(), 100)
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.is_full(), False)
        self.assertEqual(stack.top, 3)

if __name__ == "__main__":
    unittest.main()
