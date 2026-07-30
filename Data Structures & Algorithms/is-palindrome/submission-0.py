class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for i in range(len(s)) :
            if  (48<=int(ord(s[i:i+1]))<=57 or
                97<=int(ord(s[i:i+1]))<=122):
                ans += s[i:i+1]

        if ans==ans[::-1]:
            return True
        else:
            return False                               