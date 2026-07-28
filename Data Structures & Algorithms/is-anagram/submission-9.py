class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        S_dict = {}
        T_dict = {}
        
        for i in s:
            S_dict[i] = S_dict.get(i , 0) + 1



        for j in t:
            T_dict[j] = T_dict.get(j , 0) + 1

        return (S_dict == T_dict)

