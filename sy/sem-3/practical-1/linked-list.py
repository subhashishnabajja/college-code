# Node
class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None


# Linked List
class LinkedList():
    def __init__(self, data = []):
        self.head = None
        self.count = 0

        # Initialize the linked list
        for d in data:
            self.add_end(d)

    def add_start(self, data):

        new_node = Node(data) # Create a new node

        # Check if the head is None
        if self.head is None:
            self.head = new_node
            return

        new_node.ref = self.head # Change the reference of the new node the head
        self.head = new_node # Change the head to the new node
        
        self.count += 1 # Increment the count 
    def add_end(self, data):

        if self.head is None: # If the list is empty the add the node  at the begining
            self.add_start(data)
            return

        new_node = Node(data) # Create a new node
        
        # Goto the last node 
        node = self.head
        while node.ref is not None:
            node = node.ref

        node.ref = new_node
        self.count += 1 # Increment the count 

    def add_middle(self, index, data):
        # If the list is empty the add the node to the head
        if self.head is None:
            self.add_start(data)
            return
        new_node = Node(data)

        # Goto the previous node
        prev_node = None
        node = self.head
        next_node = None
        i = 0

        while i != (index - 1) :
            node = node.ref
            i += 1

        prev_node = node
        next_node = node.ref

        prev_node.ref = new_node
        new_node.ref = next_node

        print(node.data)

        self.count += 1 # Increment the count 



    def delete_start(self):
        self.head = self.head.ref
        self.count -= 1 # Decrement the counter

    def delete_end(self):
        
        # Goto the second last node
        node = self.head
        while True:
            if node.ref.ref is None:
                node.ref = None
                break

            node = node.ref
            
        self.count -= 1 # Decrement the counter

    def delete_middle(self, index):
        # Goto the prev node
        prev_node = None
        node = self.head
        next_node = None
        i = 0

        while i != (index - 1):
            node = node.ref
            i += 1
            
        
        prev_node = node
        next_node = node.ref.ref

        prev_node.ref = next_node

        self.count -= 1

    def traverse(self, cb):
        node = self.head

        while node is not None:
            cb(node.data)
            node = node.ref

    def print_list(self):
        node = self.head # Get the first node

        while node is not None:
            print(node.data, end="->")
            node = node.ref

        print("None")


# Driver code 
if __name__ == "__main__":
    linked_list = LinkedList([1,2,3,4])

    # Insertion
    linked_list.add_start(0)
    linked_list.add_end(6)
    linked_list.add_middle(5, 5)

    # Deletion
    linked_list.delete_start()
    linked_list.delete_middle(3)
    linked_list.delete_end()
 

    # Traversal
    linked_list.traverse(lambda d: print(d))



    linked_list.print_list()