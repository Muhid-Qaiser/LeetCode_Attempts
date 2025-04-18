class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        flag = True
        curr_row = 0
        row_str = [""] * numRows

        if numRows == 1:
            return s

        for c in s:
            row_str[curr_row] += c

            if curr_row == numRows-1:
                flag = False
            elif curr_row == 0:
                flag = True
            
            if flag:
                curr_row+=1
            elif not flag:
                curr_row-=1


        return "".join(row_str)


        