#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? Is time efficient compared to array
        because I am prepend. It's a matter of reassigning pointers
        instead of moving items."""
        # TODO: Push given item
        
        #prepending at head
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any

        #get the first item in stack
        if not self.list.is_empty():
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? We always know where the first node
        is LL is because it is saved to the self.head variable. Easy to access 
        and remove."""
        # TODO: Remove and return top item, if any
        
        if not self.list.is_empty():
            #first item in stack
            deleted_item = self.peek()
            #reset the head pointer to next node in list to
            #delete current head
            self.list.head = self.list.head.next
            #decrement the size by 1
            self.list.size -= 1
        else:
            raise ValueError("empty stack.")
        return deleted_item



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? Appending at the end of arrays are
        time efficient because we already know where the end is located."""
        # TODO: Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty() is False:
            #last item is n-1
            last_item = (len(self.list) -1)
            #access the last item in list
            return self.list[last_item]
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? We can get the last item in an
        array without traversing through the whole list(unlike LL) so
        all we have to do is use the pop method."""
        # TODO: Remove and return top item, if any
        if self.is_empty()
            return self.list.pop()
        else:
            raise ValueError("empty array.")


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
#Stack = LinkedStack
Stack = ArrayStack
