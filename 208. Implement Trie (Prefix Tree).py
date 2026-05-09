class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        root = self.trie
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root["."] = "."

    def search(self, word: str) -> bool:
        root = self.trie
        for c in word:
            if c not in root:
                return False
            root = root[c]
        return "." in root

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for c in prefix:
            if c not in root:
                return False
            root = root[c]
        return True


if __name__ == "__main__":
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))    
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
