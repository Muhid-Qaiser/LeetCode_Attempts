class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n <= 0:
            return True

        have_adj = False

        for idx, flower in enumerate(flowerbed):
            if flower == 1:
                have_adj = True
            elif have_adj:
                have_adj = False
            else:
                if idx < len(flowerbed) - 1 and flowerbed[idx+1] == 1:
                    continue

                have_adj = True
                n -= 1
                if n <= 0:
                    return True
        return False

        
        