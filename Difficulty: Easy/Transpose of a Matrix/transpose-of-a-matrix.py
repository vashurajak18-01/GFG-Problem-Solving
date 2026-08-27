class Solution:
    def transposeMatrix(self, arr):
        # code here
        result = []        
        for i in range(0,len(arr[0])):
            row = []
            for j in range(0,len(arr)):
                row.append(arr[j][i])
            result.append(row)
        
        return np.array(result)