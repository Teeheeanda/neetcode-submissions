class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for s1 in s:
            if s1 in ['(', '[', '{']:
                stack.append(s1)
            else:
                if stack == []:
                    return False
                
                x = stack.pop()
                if s1 == ')' and x != '(':
                    return  False
                elif s1 == '}' and x!= '{':
                    return False
                elif s1 == ']' and x!='[':
                    return False
        
        return stack == []
        