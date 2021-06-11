class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters=iter(t)
        for i in s:
            if i not in letters:
                return False
        return True