class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in s_hashmap:
                s_hashmap[char] = 1
            else:
                s_hashmap[char] += 1
        
        for char in t:
            if char not in t_hashmap:
                t_hashmap[char] = 1
            else:
                t_hashmap[char] += 1
        return t_hashmap == s_hashmap
        