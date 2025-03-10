from collections import Counter

def findSubstring(s,words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    total_words = len(words)
    substring_leng = word_len * total_words 
    word_count = Counter(words)
    result = []

    for i in range(word_len):
        left = i 
        right = i 

        current_count = Counter() 

        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len 

            if word in word_count:
                current_count[word] += 1 

                while current_count[word] > word_count[word]:
                    current_count[s[left:left + word_len]] -= 1 
                    left += word_len


                if right - left == substring_leng:
                    result.append(left)
            else:
                current_count.clear()
                left = right 

        return result 

s = "barfoothefoobarman"
words = ["foo","bar"]

print(findSubstring(s,words))