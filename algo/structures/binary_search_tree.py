from typing import Any
from dataclasses import dataclass

from algo.structures.api import BinaryTree


@dataclass
class Node:
    data: Any
    left   = None
    right  = None
    parent = None


class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        r"""Insert a new value into the tree

        Args:
            current_node: the node to start traversing from
            traversal: a string that will be recursively built

        Returns:
            traversal: the built output string
        """
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
                current_node.left.parent = current_node
            else:
                self._insert(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
                current_node.right.parent = current_node
            else:
                self._insert(current_node.right, data)

    def print_traversal(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, "")
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, "")
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, "")
        else:
            raise ValueError(f"Unknown traversal type: {traversal_type}")

    def height(self):
        r"""Get the height of the tree"""
        if self.root:
            return self._height(self.root, current_height=0)
        else:
            return 0

    def _height(self, current_node, current_height):
        r"""Return the height of the tree"""
        if current_node is None:
            return current_height
        else:
            left_subtree_height = self._height(
                current_node.left, current_height+1
            )

            right_subtree_height = self._height(
                current_node.right, current_height+1
            )

            return max(left_subtree_height, right_subtree_height)

    def find(self, data):
        if self.root:
            return self._find(self.root, data)
        else:
            return None

    def _find(self, current_node, data):
        if data == current_node.data:
            return current_node
        elif data < current_node.data and current_node.left:
            return self._find(current_node.left, data)
        elif data > current_node.data and current_node.right:
            return self._find(current_node.right, data)
        else:
            return None

    def delete(self, data):
        r"""Delete a node containing some given data"""
        return self._delete_node(self.find(data))

    def _delete_node(self, node):
        r"""Delete a given node"""
        if node is None or self.find(node.data) is None:
            # There is nothing to delete
            return None

        def min_value_node(current_node):
            r"""Find the minimum value from a given node"""
            while current_node.left:
                current_node = current_node.left
            return current_node

        def get_num_children(current_node):
            num_child = 0
            if current_node.left:
                num_child += 1
            if current_node.right:
                num_child += 1
            return num_child

        node_parent = node.parent
        num_children = get_num_children(node)

        # Case 1: delete a leaf node
        if num_children == 0:

            if node_parent:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # Case 2: there is one child node
        if num_children == 1:

            if node.left:
                child = node.left
            else:
                child = node.right

            if node_parent:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            child.parent = node_parent

        # Case 3: there are two child nodes
        if num_children == 2:
            # Recursively get the successors' data
            successor = min_value_node(node.right)
            node.data = successor.data
            self._delete_node(successor)

    def search(self, data):
        if self.root:
            return self._search(self.root, data)
        else:
            return False

    def _search(self, current_node, data):
        if data == current_node.data:
            return True
        elif data < current_node.data and current_node.left:
            return self._search(current_node.left, data)
        elif data > current_node.data and current_node.right:
            return self._search(current_node.right, data)
        else:
            return False

    def min(self):
        r"""Get the minimum data value"""
        if self.root.left is None:
            return self.root.data
        else:
            return self._seek_min(self.root)

    def _seek_min(self, current_node):
        if current_node.left is None:
            return current_node.data
        else:
            return self._seek_min(current_node.left)

    def max(self):
        r"""Get the maximum data value"""
        if self.root.right is None:
            return self.root.data
        else:
            return self._seek_max(self.root)

    def _seek_max(self, current_node):
        if current_node.right is None:
            return current_node.data
        else:
            return self._seek_max(current_node.right)

