class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        uniqueemails = set()
        
        for i in emails:
            
            name, domain = i.split('@')
            local = name.split('+')[0].replace('.','')
            uniqueemails.add(local+'@'+domain)
        return len(uniqueemails)
        