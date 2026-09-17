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


def search_time_linear(words, search_word):
    """Returns time it takes to find a word
    using a linear search in a list"""

    start = time.time()
    for word in words:
        if word == search_word:
            end = time.time()
    end = time.time()
    return end - start


def search_time_bst(words, search_word):
    """Returns time it takes to find a word
    using searing a BST"""

    start = time.time()
    words.search("zoo")
    end = time.time()
    return end - start


if __name__ == "__main__":
    words = create_word_list("words_100k.txt")
    search_word = "lunch"
    linear_time = search_time_linear(words, search_word)
    bst = create_bst(words, True)
    print(linear_time)
    bst_time = search_time_bst(bst, search_word)
    print(f"{linear_time:.10f}")

    print(f"{bst_time:.10f}")
    print(linear_time > bst_time)
