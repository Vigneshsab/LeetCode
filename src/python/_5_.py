class Solution(object):
    
    def longestPalindrome(self, s):
        res = ""
        resMaxLen = 0
        
        for i in range(len(s)):
            l, r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resMaxLen:
                    res = s[l:r+1]
                    resMaxLen = r-l+1
                l-=1
                r+=1
            
            l,r = i, i+1
            while l>=0 and r< len(s) and s[l]==s[r]:
                if (r-l+1)>resMaxLen:
                    res = s[l:r+1]
                    resMaxLen = r-l+1
                l-=1
                r+=1
        return res