class Solution(object):
    def isValid(self, s):
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:    
            if c in d:
                if stack and stack[-1] == d[c]:
                    stack.pop() 
                else:
                    return False  
            else:
                stack.append(c) 
        return not stack     
