class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hmap where key is letter count array and value is list of strings that match that count
        hmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hmap[tuple(count)].append(s)
        
        return list(hmap.values())