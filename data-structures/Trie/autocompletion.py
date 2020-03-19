# Problem and solution inspired by: https://www.youtube.com/watch?v=QGVCnjXmrNg

# TASK:
#    You are given a list of words, for instance
#    WORDS = ["atom", "anathomy", "antenna"]
#    Then you are given a pre-fix, for instance:
#    PREFIX = "an"
#    Your task is to return all possible words that PREFIX can autocomplete to.
#    In this case that would be - ["anathomy", "antenna"]

# BRUTE FORCE:
#    We could implement it with a brute force approach, where for
#    every input prefix we will want to look for all words in WORDS.
#    Time complexity would depend on the size of WORDS and the length of PREFIX
#    This means that the time complexity here is O(n * a) - where n is the size of WORDS
#    and a is the length of PREFIX. This comes down to O(2n) complexity. 

# We could make the time complexity smaller by using trie data structure. 
#
# For simplicity, in this implementation we will use hash map (Python's dict),
# instead of array for simplicity, that's a small cheat 🤫

# Also, notice that in trie's nodes the value is boolean. We want to just keep info if we reached,
# the end of word. For instance a trie with a word "cat" would look like:
#  #0: {"c": #1}, is_word = false
#  #1: {"a": #2}, is_word = false
#  #2: {"t": #3}, is_word = true
#  #3: NULL

# COMPLEXITY: 
#    By using trie data structure we can reduce the time complexity to O(n + a),
#    which could be simplified here to O(n) - time depends linearly on the number of elements in WORDS.
#    Space complexity is related to the size of the trie structure, so that's O(n).

from __future__ import annotations
from typing import List

class TrieNode:
    def __init__(self, is_word: bool):
        self.children = {}
        self.is_word = is_word

class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def get_root(self):
        return self.root

    def build(self, words: List[str]) -> Trie:
        for word in words:
            current = self.root
            for letter in word:
                if not letter in current.children:
                    current.children[letter] = TrieNode(False)
                current = current.children[letter]
            current.is_word = True
        return self

    def find_words_form_node(self, node: TrieNode, prefix: str):
        # Depth-first search
        words = []
        if node.is_word:
            words.append(prefix)
        for letter in node.children:
            words += self.find_words_form_node(node.children[letter], prefix + letter)
        return words
    
class Autocompletion:
    def __init__(self, dictionary: List[str]):
        self.dictionary = Trie().build(dictionary)

    def complete(self, prefix: str) -> List[str]:
        # Now we have to traverse as far as prefix allows us
        current = self.dictionary.get_root()
        for letter in prefix:
            if not letter in current.children:
                return []
            current = current.children[letter]
        
        # If up to this point the function did not return then we will have some
        # auto completions to "offer"
        return self.dictionary.find_words_form_node(current, prefix)

if __name__ == "__main__":
    auto = Autocompletion(["atom", "anathomy", "antenna"])
    print(auto.complete("an")) # Expect ['anathomy', 'antenna']
