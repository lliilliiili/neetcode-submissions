class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        def IfAnagrams(str1, str2)  -> Boolean:
            chk1 = {}
            chk2 = {}
            for i in str1:
                chk1[i] = chk1.get(i,0) + 1
            for j in str2:
                chk2[j] = chk2.get(j,0) + 1

            if chk1 == chk2:
                return True
            else:
                return False


        ans = []

        for n in strs:
            match = False

            for t in range(len(ans)):
                if IfAnagrams(n, ans[t][0]):
                    ans[t].append(n)
                    match = True
                    break
            if not match:
                ans.append([n])
                
        return ans