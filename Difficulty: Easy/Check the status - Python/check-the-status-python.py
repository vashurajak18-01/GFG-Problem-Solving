class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if ((a >= 0 and b < 0)and flag is False):
            return True

        elif ((a < 0 and b >= 0) and flag is False):
            return True

        elif (a < 0 and b < 0 and flag is True):
            return True
            
        return False

