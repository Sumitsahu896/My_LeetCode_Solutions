class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []
        
        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding mre types of parenthesis easier
        mapping = {"(": ")", "[": "]", "{": "}"}
        open_set = set(["(", "[", "{"])
        for i in s:
            if i in open_set:
                stack.append(i)
            elif stack and i == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []