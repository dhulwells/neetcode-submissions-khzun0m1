class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = frozenset(Counter(word).items())
            if key not in map:
                map[key] = []
            map[key].append(word)

        return list(map.values())

