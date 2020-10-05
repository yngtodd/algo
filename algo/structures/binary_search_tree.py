from typing import Any
from dataclasses import dataclass

from algo.structures.api import BinaryTree


@dataclass
class Node:
    data: Any
    left  =  None
    right =  None


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
        if current_node.data > data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        elif current_node.data < data:
            if current_node.right is None:
                current_node.right = Node(data)
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

