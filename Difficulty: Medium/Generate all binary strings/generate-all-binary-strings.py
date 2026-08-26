
class Solution:
    def binstr(self, n):
        result = []
        
        def solve(s):
            if len(s) == n:
                result.append(s)
                return
            solve(s + "0")
            solve(s + "1")
            
        solve("")
        return result