class Trie:

    def __init__(self):
        self.children = {}
        self.products = []


def suggestedProducts(products: list[str], searchWord: str) -> list[list[str]]:
    products.sort()
    # Using Prefix Tree
    # root = Trie()

    # def add(word: str):
    #     curr = root
    #     for c in word:
    #         if c not in curr.children:
    #             curr.children[c] = Trie()
    #         curr = curr.children[c]
    #         if len(curr.products) < 3:
    #             curr.products.append(word)

    # for word in products:
    #     add(word)
    # res = [[] for _ in range(len(searchWord))]
    # curr = root
    # for i, c in enumerate(searchWord):
    #     if c not in curr.children:
    #         break
    #     curr = curr.children[c]
    #     res[i] = curr.products

    # Using Binary search
    res = []
    l, r = 0, len(products) - 1
    for i, c in enumerate(searchWord):
        while l <= r and (i >= len(products[l]) or products[l][i] != c):
            l += 1
        while l <= r and (i >= len(products[r]) or products[r][i] != c):
            r -= 1
        res.append([])
        remainder = r - l + 1
        for j in range(min(3, remainder)):
            res[-1].append(products[l + j])
    return res

if __name__ == "__main__":
    products, searchWord = ["mobile","mouse","moneypot","monitor","mousepad"],  "mouse"
    print(suggestedProducts(products, searchWord))
    products, searchWord = ["havana"], "havana"
    print(suggestedProducts(products, searchWord))
