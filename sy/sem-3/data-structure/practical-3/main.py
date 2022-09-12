class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self) :
        self.head = None
        
    def add_begin(self, data):
        new_node = Node(data)

        if (self.head):
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def add_middle(self, index,data):
        if not self.head:
            return self.add_begin(data)

        new_node = Node(data)
        i = 0
        node = self.head
        while i == index - 1:
            node = node.next
            i += 1

        prev_node = node
        next_node = node.next

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = next_node
        next_node.prev = new_node


    def add_end(self, data):
        if not self.head:
            return self.add_begin(data)

        new_node = Node(data)

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        new_node.prev = node

    def delete_start(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        self.head = self.head.next


    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end="<->")
            node = node.next

        print("None")



if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.add_begin(3)
    linked_list.add_begin(1)
    linked_list.add_begin(0)

    linked_list.add_middle(1,2)
    linked_list.add_end(4)

    linked_list.delete_start()

    linked_list.print_list()