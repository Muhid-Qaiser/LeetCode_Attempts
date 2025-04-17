class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n not in visited:
            visited.add(n)
            sum_n = 0
            while n > 0:
                n1 = n % 10
                n = int(n / 10)
                sum_n += n1 ** 2
            n = sum_n

            if n == 1:
                return True

        
        return False

        