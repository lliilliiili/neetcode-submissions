class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansMap = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in  ansMap:
                ansMap[key] = []
            ansMap[key].append(s)

        ans = []

        for l in ansMap:
            ans.append(ansMap[l])

        return ans