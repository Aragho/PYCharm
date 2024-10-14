import unittest
from stack.my_stack import Stack, StackUnderFlowException






class StackoverflowException:
    pass


class TestStack (unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    def test_push(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(),10)
    def test_stack_overflow(self):
        stack = Stack()
        stack.push(10)
        with self.assertRaises(StackoverflowException):
            stack.push(20)
        
    def test_pop(self):
        self.stack.push(20)
        self.assertEqual(self.stack.pop(),20)

    def test_pop_when_empty_raises_exception(self):
        with self.assertRaises(StackUnderFlowException):
            self.stack.pop()

    def test_peek(self):
        self.stack.push(30)
        self.assertEqual(self.stack.peek(),30)
    def test_that_is_empty(self):
        self.assertTrue(self.stack.is_empty(),False)
        self.stack.push(40)
        self.assertFalse(self.stack.is_empty(),True)
    def test_size(self):
        self.stack.push(40)
        self.stack.push(50)
        self.assertEqual(self.stack.size(),2)

    def test_search(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.search(20),2)
        self.assertEqual(self.stack.search(50),-1)