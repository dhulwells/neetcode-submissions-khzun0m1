class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = frozenset(Counter(word).items())
            groups[key].append(word)

        return list(groups.values())

