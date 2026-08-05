class Solution:
    def isValid(self, s: str) -> bool:
        check = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s :

            if c not in check:
                stack.append(c)
            
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == check[c]:
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        else:
            return False