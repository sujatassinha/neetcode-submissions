class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of two strings are equal, they cannot be anagrams!
        if len(s) != len(t):
            return False
        # since the problem graurantees lower case alphabets (english), we start by defining a count array of length 26
        count = [0]*26
        # iterate through the string
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        # once the count is done, return if they are anagrams
        return not any(count)
        
        