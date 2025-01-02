from typing import List
# class Solution:
#     def vowelStrings(self, words: list[str], queries:list[list[int]]) -> list[int]:
#         vowels = 'aeiou'
#         def isVouwelString(word):
#             return word[0] in vowels and word[-1] in vowels

#         result = []

#         for l, r in queries:
#             count = sum(isVouwelString(words[i]) for i in range(l, r + 1))
#             result.append(count)


#         return result

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        kVowels = 'aeiou'
    
        prefix = [0] * (len(words) + 1)

        for i, word in enumerate(words):
            prefix[i + 1] += prefix[i] + (word[0] in kVowels and word[-1] in kVowels)

        return [prefix[r + 1] - prefix[l]
                for l, r in queries]
    
    
words = ["apple", "orange", "banana", "umbrella"]
queries = [[0, 2], [1, 3]]

sol = Solution()
print(sol.vowelStrings(words, queries))