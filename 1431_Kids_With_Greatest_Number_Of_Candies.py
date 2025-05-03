class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        bool_arr = [False] * len(candies)
        max_candies = max(candies)

        for i in range(len(candies)):

            if candies[i] + extraCandies >= max_candies:
                bool_arr[i] = True
        
        return bool_arr