class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
​
    @property
    def real_children(self):
        return self.children
​
​
class RadixTree:
    def __init__(self, *words):
        self.root = TrieNode()
        for w in set(w for w in words if w):
            self._insert(w)
​
    def _insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True
​
    def to_dict(self):
        return self._build(self.root)
​
    def _build(self, node):
        children = node.real_children
        if not children:
            return {}
​
        result = {}
        for ch, child in children.items():
            label, cur = self._merge_chain(ch, child)
            result[label] = self._build(cur)
        return result
​
    def _merge_chain(self, start_char, start_node):
        label = start_char
        cur = start_node
        while not cur.is_end and len(cur.children) == 1:
            ch, nxt = next(iter(cur.children.items()))
            label += ch
            cur = nxt
        return label, cur
​
    def __repr__(self):
        return f"RadixTree({self.to_dict()})"
​
​
def radix_tree(*words):
    return RadixTree(*words).to_dict()