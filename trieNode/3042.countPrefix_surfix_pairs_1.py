class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root 
        count = 0 
        n = len(word) 

        for i in range(n):
            prefix = word[i]
            surfix = word[n-1 - i]
            
            if (prefix, surfix) not in node.children:
                node.children[(prefix, surfix)] = TrieNode()
            node = node.children[(prefix, surfix)]
            count += node.count 
        node.count += 1 
        return count 
        
class Solution:
    def countPrefixSuffixPairs(self, words):
        trie = Trie()
        total_pairs = 0
        for word in words:
            total_pairs += trie.insert(word)

        return total_pairs
    


words = ["a","aba","ababa","aa"]
solution = Solution()
result = solution.countPrefixSuffixPairs(words)
print(f"Total Prefix-Suffix Pairs: {result}")