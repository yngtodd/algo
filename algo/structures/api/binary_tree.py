class BinaryTree:

    def preorder_print(self, current_node, traversal):
        r"""Print the pre-order traversal
        Pre-order traversal: root->left->right recursive. This
        will start with the root, then continue down the left
        sub-tree until we reach a node where there is no left
        child. We then visit all right nodes in the left sub-tree,
        and repeat for this process for the right sub-tree.
        Args:
            current_node: the node to start traversing from
            traversal: a string that will be recursively built
        Returns:
            traversal: the built output string
        """
        if current_node:
            traversal += f'{current_node.data}->'
            traversal = self.preorder_print(current_node.left, traversal)
            traversal = self.preorder_print(current_node.right, traversal)
        return traversal

    def inorder_print(self, current_node, traversal):
        r"""Print the in-order traversal
        Args:
            current_node: the node to start traversing from
            traversal: a string that will be recursively built
        Returns:
            traversal: the built output string
        """
        if current_node:
            traversal = self.inorder_print(current_node.left, traversal)
            traversal += f'{current_node.data}->'
            traversal = self.inorder_print(current_node.right, traversal)
        return traversal

    def postorder_print(self, current_node, traversal):
        r"""Print the post-order traversal
        Args:
            current_node: the node to start traversing from
            traversal: a string that will be recursively built
        Returns:
            traversal: the built output string
        """
        if current_node:
            traversal = self.postorder_print(current_node.left, traversal)
            traversal = self.postorder_print(current_node.right, traversal)
            traversal += f'{current_node.data}->'
        return traversal

    def _build_tree_string(self, current_node, current_idx, idx=False, delimiter='-'):
        r"""Build a string representation of the tree"""
        if current_node is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []

        """
        if idx:
            node_repr = f'{current_idx}{delimiter}{current_node.data}'
        else:
            node_repr = f'{current_node.data}'
        """

        if idx:
            node_repr = '{}{}{}'.format(current_idx, delimiter, current_node.data)
        else:
            node_repr = str(current_node.data)

        new_root_width = gap_size = len(node_repr)

        l_box, l_box_width, l_root_start, l_root_end = \
            self._build_tree_string(current_node.left, 2 * current_idx+1, idx, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            self._build_tree_string(current_node.right, 2 * current_idx+2, idx, delimiter)

        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('-' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append(' ' * r_root)
            line1.append('-' * (r_box_width - r_root+1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1

        new_root_end = new_root_start + new_root_width-1

        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end

    def pprint(self, idx=False, delimiter='-'):
        lines = self._build_tree_string(self.root, 0, idx, delimiter)[0]
        print('\n' + '\n'.join((line.rstrip() for line in lines)))
