"""Linked List"""


class Node:
    r"""Node of the linked list

    Args:
        data: the data held by the node
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    r"""Linked list data structure"""

    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def __len__(self):
        return self.num_nodes

    def __repr__(self):
        return f"LinkedList()"

    def to_list(self):
        r"""Convert the linked list to a Python list

        Save each data element as an element in a Python
        list.

        Returns:
            node_list: list of all the elements
        """
        node_list = []

        current_node = self.head
        while current_node:
            node_list.append(current_node.data)
            current_node = current_node.next

        return node_list

    def append(self, data):
        r"""Append some data to the end of the linked list

        Args:
            data: the data to be appended
        """
        node = Node(data)
        self.num_nodes += 1

        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = node

    def prepend(self, data):
        r"""Prepend some data to the beginning of the linked list

        Args:
            data: the data to be prepended
        """
        node = Node(data)
        self.num_nodes += 1

        head_disconnected = self.head

        self.head = node
        self.head.next = head_disconnected



