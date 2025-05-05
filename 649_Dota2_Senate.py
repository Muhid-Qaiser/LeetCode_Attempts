class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiants = []
        dires = []

        for i, x in enumerate(senate):
            if x == 'R':
                radiants.append(i)
            if x == 'D':
                dires.append(i)

        while radiants and dires:
            r = radiants.pop(0)
            d = dires.pop(0)

            if r <= d:
                radiants.append(r+n)
            else:
                dires.append(d+n)
        
        return "Radiant" if radiants else "Dire"
        