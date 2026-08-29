class Solution:
	def subsetSums(self, arr):
		# code here
		result = []

        def solve(index, total):
            if index >= len(arr):
                result.append(total)
                return 
            sum = total + arr[index]
            solve(index+1, sum)
        
            sum = total
            solve(index+1, sum)
        
        solve(0, 0)
        result.sort()
        
        return result