'''
Stack Class
'''

class Stack:
    '''
    Custom class to emulate the function of a traditional stack
    '''
    def __init__(self):
        self.items = []
        self.MAXIMUM = 100
        self.top = -1

    def is_empty(self):
        '''
        Method to see if stack is empty
        '''
        return not self.items

    def is_full(self):
        '''
        Method to see if stack is full
        '''
        return self.top == (self.MAXIMUM - 1)

    def push(self, item):
        '''
        Method to add item to stack
        '''
        self.items.append(item)
        self.top += 1

    def pop(self):
        '''
        Method to remove last item from stack
        '''
        if self.top > -1:
            self.top -= 1
            return self.items.pop()

    def peek(self):
        '''
        Method to see the value of the last object in a stack
        '''
        return self.items[len(self.items) - 1]

    def size(self):
        '''
        Method to find the length of the stack
        '''
        return len(self.items)
