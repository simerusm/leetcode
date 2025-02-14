class DictNode:
    def __init__(self):
        self.children = {} # {char: DictNode, char: DictNode, ...}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = DictNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        
        def helper(word: str, node: Optional[DictNode] = self.root) -> bool:
            for idx, char in enumerate(word):
                if char not in node.children and char != '.':
                    return False
                elif char == '.':
                    for availableNodes in node.children.values():
                        if helper(word[idx + 1:], availableNodes):
                            return True
                    return False
                else:
                    node = node.children[char]
            return node.is_end_of_word
        
        return helper(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
