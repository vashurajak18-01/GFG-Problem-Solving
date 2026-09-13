class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        # code 
        
        count = 1
        ans = 1
        arr.sort()
        dep.sort()
        i = 1
        j = 0

        while i < len(arr) and j < len(dep):
            if arr[i] <= dep [j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1

            ans = max ( ans, count)

        return ans
        