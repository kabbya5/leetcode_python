from collections import Counter 

def minWindow(s:str, t:str)->str:
    if not t or not s:
        return ''
    
    t_count = Counter(t) 
    window_count = {} 
    left = 0 
    have, need = 0, len(t_count) 
    result = ""
    min_len = float('inf')

    for right in range(len(s)):
        char = s[right] 
        window_count[char] = window_count.get(char,0) + 1 
        if char in t_count and window_count[char] == t_count[char]:
            have += 1 
        while have == need:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]
            window_count[s[left]] -= 1 

            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                have -= 1 
            left += 1 

    return result 

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))