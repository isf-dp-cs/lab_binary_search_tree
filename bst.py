# https://www.boot.dev/blog/computer-science/binary-search-tree-in-python


class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            # self._insert_recursive(self.root, value)
            curr_node = self.root
            found = False
            while found == False:
                if value < curr_node.value:
                    if curr_node.left == None:
                        found = True
                        curr_node.left = Node(value)
                    else:
                        curr_node = curr_node.left
                elif value > curr_node.value:
                    if curr_node.right == None:
                        found = True
                        curr_node.right = Node(value)
                    else:
                        curr_node = curr_node.right

    def search(self, value):
        curr_node = self.root
        found = False
        while curr_node:
            # print(curr_node)
            if value == curr_node.value:
                return True
            elif value < curr_node.value:
                curr_node = curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
        return False

    def in_order_traversal(self, node):
        if node == None:
            return
        self.in_order_traversal(node.left)
        print(node)
        self.in_order_traversal(node.right)

    # TODO: Construct method for pre-order in_order_traversal

    # TODO: Construct method for post-order in_order_traversal


if __name__ == "__main__":
    bst = BinarySearchTree()

    # TODO: insert multiple values to test the BST

    bst.insert(15)
    bst.in_order_traversal(bst.root)
