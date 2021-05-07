class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-',"").upper()
        remainder = len(s) % k
        
        first_grp = [s[0:remainder]]
        other_grps = [s[i:i+k] for i in range(remainder, len(s),k)]
        
        if remainder:
            return "-".join(first_grp+other_grps)
        return "-".join(other_grps)