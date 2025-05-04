class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        hashmap = defaultdict(int)
        count = 0

        for row in grid:
            hashmap[str(row)] += 1

        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += hashmap[str(col)]

        return count



        