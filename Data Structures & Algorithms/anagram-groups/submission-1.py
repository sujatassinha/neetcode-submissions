class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagrams when sorted become identical. 
        # So start by defining a hashmap where each key is a sorted version of an anagram. So all anagrams can be put as values under the same key
        hmap = defaultdict(list)
        # then go through each string in strs and sort it
        # that becomes key
        # under the same key, all anagrams will go that belongs to that key
        for s in strs:
            sortedS = ''.join(sorted(s))
            hmap[sortedS].append(s)
        return list(hmap.values())