class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height) == 0 :
            return 0
        elif len(height) == 1:
            return list[0]
        
        left, right = 0, len(height)-1
        max_area = -1

        while left < right:
            curr_width = right - left
            curr_height = min(height[left], height[right])
            area = curr_width * curr_height

            if max_area < area:
                max_area = area

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return max_area