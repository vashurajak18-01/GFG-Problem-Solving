class Solution:
    def countTriplets(self, sum, arr):
        #code here
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            left = i+1
            right = n-1
            
            while left<right:
               
                total = arr[i]+arr[left]+arr[right]
                if total >= sum:
                    right -=1
                else:
                    ans= ans+(right-left)
                    left += 1
                
        return ans            