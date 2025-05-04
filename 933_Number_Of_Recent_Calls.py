class RecentCounter:

    def __init__(self):
        self.queue = []
        self.count = 0
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[self.count] < t - 3000:
            self.count += 1
        return len(self.queue) - self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)