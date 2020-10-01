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

    def insert_after(self, key, data):
        r"""Add a node after a node of a given `key` value

        Args:
            key: the node the data should be added after
            data: the data to be added
        """
        node = Node(data)

        current_node = self.head
        while current_node.next and current_node.data != key:
            current_node = current_node.next

        if current_node.next:
            node_disconnected = current_node.next
            current_node.next = node
            node.next = node_disconnected
            self.num_nodes += 1

    def insert_before(self, key, data):
        r"""Add a node beore a given `key`

        Args:
            key: the value of a node before which the data
                 will be added
            data: the data to be added
        """
        if self.head.data == key:
            self.prepend(data)

        else:
            current_node = self.head
            next_node = current_node.next
            while next_node.next and next_node.data != key:
                current_node = current_node.next
                next_node = next_node.next

            if next_node.data == key:
                node = Node(data)
                self.num_nodes += 1
                current_node.next = node
                node.next = next_node

    def pop_head(self):
        r"""Remove the data at the head"""
        self.head = self.head.next
        self.num_nodes -= 1

    def delete(self, data):
        r"""Delete a node with a given data value

        Args:
            data: the value of the node to be deleted
        """
        if self.head.data == data:
            self.pop_head()

        prev = None
        current_node = self.head

        while current_node.next and current_node.data != data:
            prev = current_node
            current_node = current_node.next

        if current_node.data == data:
            prev.next = current_node.next

