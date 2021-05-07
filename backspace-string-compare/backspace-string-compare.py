class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(S):
            ans = []
            for char in S:
                if char != '#':
                    ans.append(char)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)