class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search_helper(self, word_index: int, word: str, node: TrieNode):
        for i in range(word_index, len(word)):
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if self.search_helper(i+1, word, child):
                        return True
                return False
            elif c in node.children:
                node = node.children[c]
            else:
                return False
        return node.is_word
        
    
    def search(self, word: str) -> bool:
        node = self.root
        return self.search_helper(0, word, node)
