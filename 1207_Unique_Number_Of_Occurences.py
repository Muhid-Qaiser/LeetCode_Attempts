class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        import numpy as np

        _, counts = np.unique(arr, return_counts=True)

        return len(counts) == len( set(counts) )
        