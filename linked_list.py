class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    def append(self, data):
        """ Append a node to the end of the list """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """ Print all elements in the list """
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

# Example usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

llist.print_list()  # Output: 1 -> 2 -> 3 -> None
