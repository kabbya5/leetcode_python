from typing import List 

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = [] 
        line, line_length = [], 0 
        i = 0 

        while i < len(words):
            word = words[i]
            if line_length + len(word) + len(line) > maxWidth:
                spaces = maxWidth - line_length 
                for j in range(spaces):
                    line[j % (len(line) - 1 or 1)] += " "
                res.append("".join(line))

                line, line_length = [], 0

            line.append(word) 
            line_length += len(word) 
            i += 1 

        res.append(" ".join(line).ljust(maxWidth))
        return res
    
s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = s.fullJustify(words, maxWidth)

for line in output:
    print(f'"{line}"') 
