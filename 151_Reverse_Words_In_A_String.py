class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        
        return " ".join( s.split()[::-1] )
        