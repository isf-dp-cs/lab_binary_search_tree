import time
from bst import BinarySearchTree
from random import shuffle


def create_word_list(file):
    """Returns a list of words"""

    f = open(file, "r")
    words = []
    for line in f.readlines():
        words.append(line.strip())
    return words


def create_bst(words, balanced):
    """Returns a BST of the words"""

    bst = BinarySearchTree()

    if balanced == True:
        shuffle(words)

    for word in words:
        bst.insert(word)
    return bst


if __name__ == "__main__":
    words = create_word_list("words_100k.txt")
    bst = create_bst(words, True)

    # TODO: Compare the search times between the linear list
    # and the BST balanced and the BST unbalanced
