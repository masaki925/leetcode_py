class Node:
    def __init__(self, val: str):
        self.val = val
        self.end_of_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node("dummy")
        pass

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]

        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        if cur.end_of_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()

obj.insert("apple")
print(f"{obj.search('apple')=}")
print(f"{obj.search('app')=}")
print(f"{obj.startsWith('app')=}")
obj.insert("app")
print(f"{obj.search('app')=}")
