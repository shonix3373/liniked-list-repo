class node:
    data = None
    next_node = None 

    def __init__(self, data): # constructor
        self.data = data

    def __repr__(self): # representation
        return "<Node data: %s>" % self.data 
    
class linked_list:
    head = None

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns list's length
        takes linear time - O(n)

        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count