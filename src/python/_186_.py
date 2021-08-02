class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverse (s, left, right):
            while left<right:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
            return s
        reverse(s, 0, len(s)-1)
        i,left = 0, 0
        n = len(s)
        while i<n:
            if s[i]==" ":
                reverse(s, left, i-1)
                left = i+1
            elif i == len(s)-1:
                reverse(s, left, i)
            i+=1
                
        