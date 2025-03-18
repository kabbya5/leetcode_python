from math import gcd

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    gcd_length = gcd(len(str1), len(str2)) 
    return str1[:gcd_length]  


print(gcdOfStrings("ABCABC", "ABC"))  
print(gcdOfStrings("ABABAB", "ABAB")) 
print(gcdOfStrings("LEET", "CODE"))    
