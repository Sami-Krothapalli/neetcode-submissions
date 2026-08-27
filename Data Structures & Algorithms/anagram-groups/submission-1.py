from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        listfinal = []

        for word in strs:
            sig = ''.join(sorted(word))
            anagram_map[sig].append(word)
        
        for sig in anagram_map:
            listfinal.append(anagram_map[sig])
        return listfinal


        