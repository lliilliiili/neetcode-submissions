class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for n in  nums:
            map[n] = map.get(n, 0)+1

        key_list = sorted(map.keys(), key = lambda x: map[x], reverse = True)

        return key_list[:k]