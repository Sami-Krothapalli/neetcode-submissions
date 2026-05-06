class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_S = {}
        count_T = {}

        for char_s in s:
                if char_s not in count_S:
                    count_S[char_s] = 1
                else:
                    count_S[char_s] += 1
        for char_t in t:
                if char_t not in count_T:
                    count_T[char_t] = 1
                else:
                    count_T[char_t] += 1
            
        return count_S == count_T
