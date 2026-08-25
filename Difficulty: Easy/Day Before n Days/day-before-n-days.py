class Solution:
    def nthDay(self, d: int, n: int) -> int:
        """ code here """
        return (d-n) % 7
