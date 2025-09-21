class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        reversedX = x[::-1]
        if x == reversedX:
            return True
        return False
